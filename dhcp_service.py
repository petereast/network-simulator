# DHCP - a service module for assigning addr's

from service import service
from packet import packet

class dhcp_service(service):
    def __init__(self, parent):

        self.type = "Generic DHCP Server"

        self.addrpool = [hex(x) for x in range(1, 0xff)]
        self.addrmap = dict()

        self.parent = parent

    def _process_dhcp_request(self, request):
        #The requests will follow the format:
        #"CAN I HAZ AN ADDRESS PLS"

        if request.ptype == "dhcp-request":
            source_ifaceid = request.from_ifaceid
            try:
                addr = self.addrpool.pop(0)
                # TODO: Send a message "HERE U GO U CAN HAZ THIS ADDRESS: `{0}`"
                self.addrmap[addr] = source_ifaceid

                #Record this association with the routing_table service

                r = self.parent._getService("routing")
                r.assoc(source_ifaceid, addr)

                return "DHCPSUCCESS: {0}".format(addr)
                 #The returned value is sent back to the original host
            except IndexError:
                # All outta addresses
                print("[Warn ] This dhcp server is all outta addresses")
                return "DHCPERROR1: No more addresses"

    def generate_dhcp_packet(self, request):
        return packet(payload = self._process_dhcp_request(request),
            to_ifaceid = request.from_ifaceid,
            from_ifaceid = request.to_ifaceid,
            ptype="dhcp-reply")

class dhcp_client(service):
    def __init__(self, parent):
        self.type = "Generic DHCP Client"
        self.parent = parent
        self.active_interface_name = None
        self.active_interface = None

        self.found_connection = False

    def _config(self, interface_name = None):
        if interface_name != None:
            self.active_interface_name = interface_name
            self.active_interface = self.parent.getInterface(interface_name)

    def generate_request_packet(self, interface_name):
        print("[DEBUG]", self.parent.getInterface(interface_name).iid)
        return packet(payload="DHCPREQUEST",
            from_ifaceid=self.parent.getInterface(interface_name).iid,
            to_addr="BCAST",
            ptype="dhcp-request")

    def parse_response(self, response):
        if response == None:
            print("[WARN ] dhcp-request: no response")
        elif response.ptype == "dhcp-reply" and response.payload[:11] == "DHCPSUCCESS":
            self._set_addr(response.payload[13:])
            self.found_connection = True
        elif response.ptype == "dhcp-reply" and response.payload[:9] == "DHCPERROR":
            print("[ERROR]", response.payload)
        elif response.ptype != "dhcp-reply":
            pass
        else:
            print("[ WTF ] Eh? This shouldn't happen")
        pass

    def _set_addr(self, addr):
        self.parent.getInterface(self.active_interface_name).addr = addr

    def tick(self):
        if self.active_interface_name != None and not self.found_connection:
            self.parent.getInterface(self.active_interface_name).send(
                self.generate_request_packet(self.active_interface_name))
            # This next bit should wait for a recvHook
    def getResponse(self):
        self.parse_response(
            self.parent.getInterface(self.active_interface_name).recv()
        )

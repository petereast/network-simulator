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
        payload = self._process_dhcp_request(request)

        return packet(payload, request.from_ifaceid, request.to_ifaceid, ptype="dhcp-reply")

class dhcp_client(service):
    def __init__(self, parent):
        self.type = "Generic DHCP Client"
        self.parent = parent
        self.active_interface_name = None
        self.active_interface = None

    def __config(self, interface_name = None):

        if interface_name != None:
            self.active_interface_name = interface_name

            self.active_interface = self.parent.getInterface(interface_name)


    def generate_request_packet(self, interface_name):
        return packet("DHCPREQUEST", from_ifaceid=self.parent.getInterface(interface_name).iid, to_addr="BCAST")

    def _set_addr(self, addr):
        self.parent.getInterface(interface_name).addr = addr

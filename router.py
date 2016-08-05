# Router - a machine with 2 network interfaces, that handles DHCP, NAT and other stuff

from machine import machine
from node import interface

#Import services
from dhcp_service import *
from routing_table import *

class router(machine):
    def __init__(self):
        self.type = "Generic Router"

        self._addInterface(name="internal-iface")
        self.getInterface("internal-iface").flags.append("Router Internal")

        self._addInterface(name="external-iface")
        self.external_iface = interface(self)

        # Initialise the services for this machine
        self._addService(dhcp_service, "dhcp-server")
        self._addService(routing_table, "routing")

    def recvHook(self, ifaceid):
        if ifaceid == self.getInterface("internal-iface").iid:
            recvd_packet = self.getInterface("internal-iface").recv()
            print("[INFO ] Getting internal stuff to route outwards")

            if recvd_packet.ptype == "dhcp-request":
                d = self._getService("dhcp-server")
                result = d.generate_dhcp_packet(recvd_packet)
                self.getInterface("internal-iface").send(result)


            # This is the internal routing for this network
            # add code for dhcp etc here.

        elif ifaceid == self.getInterface("external-iface").iid:
            # Deal with the stuff from the outside
            pass

# Router - a machine with 2 network interfaces, that handles DHCP, NAT and other stuff

from machine import machine
from node import interface

#Import services
from dhcp_service import *
from routing_table import *

class router(machine):
    def __init__(self):
        self.type = "Generic Router"

        self.internal_iface = interface(self)
        self.internal_iface.flags.append("Router Internal")
        # TODO: Make up some sort of enum for the interface flags

        self.external_iface = interface(self)

        # Initialise the services for this machine
        self._addService(dhcp_service, "dhcp-server")
        self._addService(routing_table, "routing")

    def recvHook(self, ifaceid):
        if ifaceid == self.internal_iface.iid:
            recvd_packet = self.internal_iface.incoming_buffer.pop(0)
            print("[INFO ] Getting internal stuff to route outwards")

            if recvd_packet.ptype == "dhcp-request":
                d = self._getService("dhcp-server")
                result = d.process_dhcp_request(recvd_packet)


            # This is the internal routing for this network
            # add code for dhcp etc here.

        elif ifaceid == self.external_iface.iid:
            # Deal with the stuff from the outside
            pass

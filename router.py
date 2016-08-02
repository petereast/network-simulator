# Router - a machine with 2 network interfaces, that handles DHCP, NAT and other stuff

from machine import machine
from node import interface

class router(machine):
    def __init__(self):
        self.type = "Generic Router"

        self.internal_iface = interface(self)
        self.internal_iface.flags.append("Router Internal")
        # TODO: Make up some sort of enum for the interface flags

        self.external_iface = interface(self)

    def recvHook(self, ifaceid):
        if ifaceid == self.internal_iface.iid:
            print("[INFO ] Getting internal stuff to route outwards")
            # This is the internal routing for this network
            # add code for dhcp etc here.

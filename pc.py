# pc.py - this is a basic machine, designed to simulate a standard client pc

from machine import machine
from node import interface

class pc(machine):
    def __init__(self):
        print("[Info ] I MADE A MACHine")

        self.iface = interface(self)

        # TODO: Make a dhcp client service.
        self._addService(None, "dhcp-client")

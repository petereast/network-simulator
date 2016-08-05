# pc.py - this is a basic machine, designed to simulate a standard client pc

from machine import machine
from node import interface
from dhcp_service import dhcp_client

class pc(machine):
    def __init__(self):
        print("[Info ] I MADE A MACHine")

        self.iface = interface(self)

        # Flags initialisation
        self.flags.append("auto-iface")

        # TODO: Make a dhcp client service.
        self._addService(dhcp_client, "dhcp-client")

        # TODO: Change the way machines register interfaces

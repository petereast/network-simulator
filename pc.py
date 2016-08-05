# pc.py - this is a basic machine, designed to simulate a standard client pc

from machine import machine
from node import interface
from dhcp_service import dhcp_client

class pc(machine):
    def start(self):
        print("[Info ] I MADE A MACHine")

        self._addInterface(interface(self))

        #print("[DEBUG] ", self._interfaces_lookup)
        # Flags initialisation
        self.flags.append("auto-iface")

        # TODO: Make a dhcp client service.
        self._addService(dhcp_client, "dhcp-client")
        self._getService("dhcp-client")._config(interface_name = self.getInterface().name)

        #self.serviceTick()

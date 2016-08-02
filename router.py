# Router - a machine with 2 network interfaces, that handles DHCP, NAT and other stuff

from machine import machine

class router(machine):
    def __init__(self):
        self.type = "Generic Router"

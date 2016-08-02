# Switch - defines a simple network switch with 16 ports

from machine import machine
import node

class switch(machine):
    def __init__(self):
        self.type = "Generic Switch"

        self.ifaces = [node.interface(self) for i in range(16)]
        # Populate a lookup table of the interfaces
        self.ifaces_lookup = dict()
        for index, iface in enumerate(self.ifaces):
            self.ifaces_lookup[iface.iid] = index

    def connect(self, peer_iface):
        for index, iface in enumerate(self.ifaces):
            if iface.peer == None:
                self.ifaces[index].connect(peer_iface)
                print("Connected to {0} (port: {1})".format(iface.iid, index))
                return 0
        print("[Warn ] All of the ports are in use")

    def recvHook(self, ifaceid):
        print("Recieved a packet from {0}".format(ifaceid))
        print(self.ifaces[self.ifaces_lookup[ifaceid]].incoming_buffer)

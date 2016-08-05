# Switch - defines a simple network switch with 16 ports

from machine import machine
import node

class switch(machine):
    def __init__(self, ports=16):
        self.type = "Generic Switch"

        # Create 'physical' interfaces for this switch
        self.ifaces = [node.interface(self) for i in range(ports)]
        # This will contain the address for a router connected to this switch
        self.gateway = None
        # Populate a lookup table of the interfaces
        self.ifaces_lookup = dict()
        for index, iface in enumerate(self.ifaces):
            self.ifaces_lookup[iface.iid] = index

    def connect(self, peer_iface):
        for index, iface in enumerate(self.ifaces):
            if iface.peer == None:
                self.ifaces[index].connect(peer_iface)
                # Check if a router has been connected
                if "Router Internal" in self.ifaces[index].peer.flags:
                    print("[Info ] Switch iface {2} connected to {0} [Router] (port: {1})".format(iface.peer.iid, index, iface.iid))
                    self.gateway = self.ifaces[index].iid
                else:
                    print("[Info ] Switch iface {2} connected to {0} (port: {1})".format(iface.peer.iid, index, iface.iid))
                return 0
        print("[Warn ] All of the ports are in this switch are in use")

    def recvHook(self, ifaceid):
        print("[Info ] Switch recieved a packet from {0}".format(ifaceid))
        recvd_packet = self.ifaces[self.ifaces_lookup[ifaceid]].incoming_buffer.pop(0)
        # Check if the recieved packet is destined for an interface connected to
        # this switch

        destport = None

        for l_iface in self.ifaces:
            if l_iface.peer.iid == recvd_packet.to_ifaceid:
                destport = self.ifaces_lookup[l_iface.iid]
                break

        if destport != None:
            self.ifaces[destport].send(recvd_packet)
        elif recvd_packet.to_addr == "BCAST":
            #This is a broadcast packet - send it to all the connected hosts
            for out_iface in self.ifaces:
                out_iface.send(recvd_packet)

        else:
            if self.gateway != None:
                print("[INFO ] Sending the packet to a router")
                self.ifaces[self.ifaces_lookup[self.gateway]].send(recvd_packet)
                #give this to a router to handle this
            else:
                print("[WARN ] No router connected")

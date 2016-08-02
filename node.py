# This class represents a single network interface connected to this virtual
# network

import interface_ids, packet

class interface:
    def __init__(self, parent):
        print("Created an interface")

        self.peer = None

        self.iid = interface_ids.generate_interface_id()
        self.addr = '' #find a way to generate an address
        print("interface_id: {0}".format(self.iid))

        self.parent = parent
        # self.parent is the 'device' which has this interface
        self.incoming_buffer = []
        # The parent can take things from the incoming_buffer, and other interfaces
        # can put things into the incoming buffer

        self.outgoing_buffer = []
        # The parent can put things into the outgoing_buffer and other interfaces
        # can take things from the outgoing buffer

        #TODO: Define a class for a packet.

    def connect(self, peer):
        # Connect this interface to it's peer
        # (This represents a physical connection)
        if self.peer != None and peer.peer != None:
            print("[Error] A connection already exists")
        elif self.peer == peer:
            print("[Warn ] This node is already connected to this peer")
        else:
            self.peer = peer
            self.peer.peer = self

    def send(self, packet):
        # Add a packet to the incoming buffer of the peer

        if self.peer != None:
            self.peer.incoming_buffer.append(packet)
            #TODO: Add something to respond to the packets

            self.peer.send_alert()
        else:
            print("[Error] No connection")
        pass

    def send_alert(self):
        print("Gotit! ({0})".format(self.iid))

# This class represents a single network interface connected to this virtual
# network

import interface_ids, packet

class interface():
    def __init__(self, parent, name = ''):
        self.peer = None

        self.iid = interface_ids.generate_interface_id()
        self.addr = '' #find a way to generate an address
        #print("[Info ] Created interface_id: {0}".format(self.iid))

        self.parent = parent
        # self.parent is the 'device' which has this interface
        self.incoming_buffer = []
        # The parent can take things from the incoming_buffer, and other interfaces
        # can put things into the incoming buffer

        self.outgoing_buffer = []
        # The parent can put things into the outgoing_buffer and other interfaces
        # can take things from the outgoing buffer

        # This'll contain metadata about the interface
        self.flags = []
        
        self.name = name

        #  Check if the parent machine has the 'auto-iface' flag.
        if "auto-iface" in self.parent.flags:
            pass
    def auto_connect(self, peer_pc):
        pass
    def connect(self, peer):
        # Connect this interface to it's peer
        # (This represents a physical connection)
        if self.peer != None and peer.peer != None:
            print("[Info ][Error] A connection already exists")
        elif self.peer == peer:
            print("[Info ][Warn ] This node is already connected to this peer")
        else:
            self.peer = peer
            self.peer.peer = self

    def send(self, outgoing_packet):
        # Add a packet to the incoming buffer of the peer

        # Make sure an actual packet is being sent
        if type(outgoing_packet) != packet.packet:
            print("[Warn ] This could be an issue, you've sent something which isn't a packet")

        if self.peer != None:
            self.peer.incoming_buffer.append(outgoing_packet)
            #TODO: Add something to respond to the packets
            try:
                # Trigger the peer's parent with the packet
                self.peer.parent.recvHook(self.peer.iid)
            except NameError:
                self.peer.send_alert()
            except AttributeError:
                print("[Info ] Sending to nothing")
        else:
            print("[Info ][Error] No connection")
        pass

    def recv(self, i=0):
        try:
            return self.incoming_buffer.pop(i)
        except IndexError:
            print("[INFO ] Recv from empty buffer")

    def send_alert(self):
        print("[Info ]Gotit! ({0})".format(self.iid))

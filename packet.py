# This class defines a packet of data

class packet:
    def __init__(self, payload, to_ifaceid, from_ifaceid, to_addr='', from_addr=''):
        """A Container for data passed between interfaces"""
        self.to_ifaceid = to_ifaceid
        self.from_ifaceid = from_ifaceid
        self.payload = payload

        self.to_addr = to_addr
        self.from_addr = from_addr

        self.size = len(payload)

class encapsulated_packet:
    def __init__(self):
        pass

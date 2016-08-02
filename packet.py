# This class defines a packet of data

class packet:
    def __init__(self, to, pfrom, payload):
        """A Container for data passed between interfaces"""
        self.to = to
        self.pfrom = pfrom
        self.payload = payload
        self.size = len(payload) 

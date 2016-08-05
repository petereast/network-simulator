# Routing table - stores the info about the routes & stuff

from service import service


class routing_table(service):
    def __init__(self, parent):

        self.table = dict()
        pass

    def assoc(self, source_ifaceid, addr):
        self.table[addr] = source_ifaceid

    def resolve_address(self, addr):
        return self.table[addr]

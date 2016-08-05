# machine - defines a vitrual machine with zero or more network interfaces

import service, node

class machine:
    _services = []
    _services_lookup = dict()
    flags = []
    _interfaces = []
    _interfaces_lookup = dict()
    def __init__(self):
        self.type = "Generic Machine"

    def recvHook(self, ifaceid):
        print("[Info ] Parent RECVHOOK")

    def _addService(self, added_service, name = None):
        # if type(added_service) != service.service:
        #     print("[Error] This isn't a valid service.")
        #     return 0
        if name == None:
            print("[Info ] Adding Service {0}".format(added_service.type))
            name = added_service.type
        else:
            print("[Info ] Adding Service", name)

        self._services.append(added_service(self))
        self._services_lookup[name] = len(self._services)-1

    def _getService(self, name):
        try:
            return self._services[self._services_lookup[name]]
        except KeyError:
            return None

    def _addInterface(self, interface = node.interface, name=None):

        if name == None:
            # Generate an interface name
            name = "auto{0}".format(len(self._interfaces)-1)
        self._interfaces.append(interface(self))

        self._interfaces_lookup[name] = len(self._interfaces)-1

    def getInterface(self, name):
        try:
            return self._interfaces[self._interfaces_lookup[name]]
        except KeyError:
            return None

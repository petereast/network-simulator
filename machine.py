# machine - defines a vitrual machine with zero or more network interfaces

import service

class machine:
    def __init__(self):
        self.type = "Generic Machine"

        self._services = []
        self._services_lookup = dict()

        pass

    def recvHook(self, ifaceid):
        print("[Info ] Parent RECVHOOK")

    def _addService(self, service, name = None):

        if type(service) != service.service:
            print("[Error] This isn't a valid service.")
            return 0
        if name == None:
            print("Adding Service {0}".format(service.type))
        else:
            print("Adding Service", name)

        self._services.append(service(self))
        self._services_lookup[name] = len(self._services)-1

    def _getService(self, name):
        return self._services[self._services_lookup[name]]

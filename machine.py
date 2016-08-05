# machine - defines a vitrual machine with zero or more network interfaces

import service

class machine:
    _services = []
    _services_lookup = dict()
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

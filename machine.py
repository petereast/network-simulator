# machine - defines a vitrual machine with zero or more network interfaces

import service
from node import interface

class machine:
    _services = []
    _services_lookup = dict()
    flags = []
    _interfaces = []
    _interfaces_lookup = dict()

    _startmessage = True
    def __init__(self):
        self.type = "Generic Machine"
        self._services = []
        self._services_lookup = dict()
        self.flags = []
        self._interfaces = []
        self._interfaces_lookup = dict()

        # Each machine needs a start function
        self.start()

    def start(self):
        if self._startmessage:
            print("[INFO ] Don't forget to define your start function!")
            self._startmessage = False
        pass

    def recvHook(self, ifaceid):
        print("[Info ] Parent RECVHOOK", ifaceid)

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

    def serviceTick(self):
        for s in self._services:
            s._tick_handler()

    def _addInterface(self, new_interface, name = None):

        self._interfaces.append(new_interface)

        if name == None:
            # Generate an interface name
            name = "auto{0}".format(len(self._interfaces)-1)

        self._interfaces[-1].name = name

        self._interfaces_lookup[name] = len(self._interfaces)-1

    def getInterface(self, name=''):
        try:
            return self._interfaces[self._interfaces_lookup[name]]
        except KeyError:
            try:
                print("[Warn ] Interface not found, using default")
                return self._interfaces[0]
            except IndexError:
                print("[Warn ] No interfaces associated with this host")
                return None

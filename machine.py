# machine - defines a vitrual machine with zero or more network interfaces

class machine:
    def __init__(self):
        self.type = "Generic Machine"
        pass

    def recvHook(self, ifaceid):
        print("[Info ] Parent RECVHOOK")

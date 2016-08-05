# Service - defines a class for 'software' modules, executed by machines

class service:
    ticks = 0
    tickdelay = 0
    tickwarning_display = True
    type = "Generic Service"
    def _config(self, **args):
        print("CONFIG!")

    def _tick_handler(self):
        self.ticks+= 1
        if self.tickdelay != 0:
            self.tickdelay-=1
        else:
            self.tick()

    def tick(self):
        if self.tickwarning_display:
            print("[DEBUG] Service tick")
            print("[DEBUG] This service ({0}) hasn't got a tick function".format(self.type))
            self.tickwarning_display = False
        # To be involked by the network class - basically giving each service
        # a chance to be updated - an event
        # the available events to a service will be:
        #   tick - after x seconds, do this action (as controlled by network)
        #   called by host - an action called by the host instance such as onRecv

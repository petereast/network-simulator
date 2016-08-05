# network.py - a module to represent a network and it's 'animation'

import time

import node, switch, packet, router, pc
from machine import machine

class network:
    def __init__(self):
        # The pool contains all
        self.pool = []

        self.pool_lookup = dict()

        self.tick_delay = 1.0


    def addMachine(self, machine = None, name=''):
        self.pool.append(machine)
        self.pool_lookup[name] = len(self.pool)-1

    def _netTick(self):
        for m in self.pool:
            m.serviceTick()
        time.sleep(self.tick_delay)

    def start(self):
        while True:
            self._netTick()

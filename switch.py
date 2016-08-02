# Switch - defines a simple network switch with umpteen ports

from machine import machine

class switch(machine):
    def __init__(self):
        self.type = "Generic Switch"

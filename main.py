#!/usr/bin/env python3

import sys

import node, switch, packet
from machine import machine

def main():
    print("[Info ]network-simulator")
    print("[Info ]Peter's network simulator, as produced during a holiday")
    test()
def test():
    a, b, c, d, f = node.interface(machine()), node.interface(machine()),node.interface(machine()), node.interface(machine()), node.interface(machine())
    e = switch.switch()
    a.connect(b)
    a.send(packet.packet("hello", None, None))
    e.connect(c)
    e.connect(d)
    e.connect(f)
    print(c.iid)
    c.send(packet.packet("Hello", "IFACE0x3", c.iid))

main()

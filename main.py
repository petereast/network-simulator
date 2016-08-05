#!/usr/bin/env python3

import sys

import node, switch, packet, router, pc
from machine import machine

import network

def main():
    print("[Info ] network-simulator")
    print("[Info ] Peter's network simulator, as produced during a holiday")
    test()
def test():
    a, b, c, d, f = node.interface(machine()), node.interface(machine()),node.interface(machine()), node.interface(machine()), node.interface(machine())
    e = switch.switch()
    # a.connect(b)
    # a.send(packet.packet("hello", None, None))
    # e.connect(c)
    # e.connect(d)
    # e.connect(f)
    # c.send(packet.packet("Hello", d.iid, c.iid))
    # c.send(packet.packet("Goodbye", f.iid, c.iid))

    n = network.network()

    r1 = router.router()
    e.connect(r1.getInterface("internal-iface"))
    n.addMachine(r1)


    p = pc.pc()
    p1 = pc.pc()
    e.connect(p.getInterface("auto0"))
    e.connect(p1.getInterface("auto0"))
    n.addMachine(p)
    n.addMachine(p1)

    print(p.getInterface("auto0").addr)
    print(p1.getInterface("auto0").addr)

    n.start()
main()

#!/usr/bin/env python3

import sys

import node, switch

def main():
    print("network-simulator")
    print("Peter's network simulator, as produced during a holiday")
    test()
def test():
    a, b, c, d, f = node.interface(None), node.interface(None),node.interface(None), node.interface(None), node.interface(None)
    e = switch.switch()
    a.connect(b)
    a.send("hello")
    b.send("goodbye")

    e.connect(c)
    e.connect(d)
    e.connect(f)

    c.send("Hello")
    print(c.peer.iid)

main()

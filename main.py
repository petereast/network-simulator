#!/usr/bin/env python3

import sys

import node

def main():
    print("network-simulator")
    print("Peter's network simulator, as produced during a holiday")
    test()
def test():
    a, b = node.interface(None), node.interface(None)

    a.connect(b)
    a.send("hello")
    b.send("goodbye")


main()

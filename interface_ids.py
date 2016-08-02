# This module contains functions for generating unique identifiers for the
# virtual interfaces

import random

incremental_id = 0

def generate_interface_id():
    global incremental_id
    interface_id = ""#.join([random.choice(list("ABCDEF")) for x in range(12)])
    interface_id += hex(incremental_id)
    incremental_id+=1
    return "IFACE{0}".format(interface_id)

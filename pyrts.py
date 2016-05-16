__author__ = 'root'

import sys
import socket

address = sys.argv[1]
startport = int(sys.argv[2])
endport = int(sys.argv[3])
only_open = sys.argv[4]

"""Simple port scanner, needs root privileges to run on the first 1024 ports"""
for x in range(startport, endport + 1):
    portstatus = None
    try:
        sock = socket.create_connection((address, x),50)
        portstatus = "open."
    except:
        print(sys.exc_info())
        portstatus = "closed."
    finally:
        if only_open == "y":
            if portstatus == "open.":
                print("Port " + str(x) + " is " + portstatus)
        else:
            print("Port " + str(x) + " is " + portstatus)
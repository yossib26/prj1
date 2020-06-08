#!/usr/bin/env python

import os
from scapy.all import *

print("---------------------------------------")
print(sys.argv)

if len(sys.argv) == 2:
    iface = str(sys.argv[1])
else:
    iface = "wlan8"

# os.system("ifconfig " + iface + " down")
# os.system("iwconfig " + iface + " mode monitor")
# os.system("ifconfig " + iface + " up")


print("[+] Sniffing on interface " + iface + ": ")

while True:
    for channel in range(1, 14):
        # os.system("ipconfig " + iface + " channel " + str(channel))
        print("[+] Sniffing on channel " + str(channel))
        # sniff(iface=iface, prn=handle_packet, count=10, timeout=3, store=0)



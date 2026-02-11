#!/usr/bin/env python
interface="gigabitethernet0/0"
address="192.168.10.1"
mask="255.255.255.0"

print("enable\n"+"conf t\n")
print("interface"+interface)
print("ip address "+address+""+mask+"\n")

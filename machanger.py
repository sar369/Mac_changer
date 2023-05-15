#!/usr/bin/env python

import subprocess

print("Welcome to Mac changer")
print(".....................\n")

interface = input("Your interface: ")
new_mac = input("Enter New Mac address: ")

print("[+] Changing Mac address for " + interface + " to " + new_mac)
subprocess.call("ifconfig ", interface, " down")
subprocess.call("ifconfig ", interface, " hw", "ether ",  new_mac)
subprocess.call("ifconfig ", interface, " up")



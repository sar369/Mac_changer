
#!/usr/bin/env python

import subprocess

print("Welcome to Mac changer")
print(".....................\n")

interface = input("Your interface: ")
mac = input("Enter New Mac address: ")

print("[+] Changing the Mac address " + interface + " to " + mac)


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac])
subprocess.call(["ifconfig", interface, "up"])

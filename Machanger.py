#!/usr/bin/env python

import subprocess
import optparse

def get_arg():
 parser = optparse.OptionParser()

 parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac address")
 parser.add_option("-m", "--mac", dest="new_mac", help="Its Mac address")

 return  parser.parse_args()


def change_mac(interface, new_mac):
 print("[+] Changing Mac address for " + interface + " to " + new_mac)
 subprocess.call("ifconfig " + interface + " down", shell=True)
 subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
 subprocess.call("ifconfig " + interface + " up", shell=True)


(options,y) = get_arg()
change_mac(options.interface,options.new_mac)


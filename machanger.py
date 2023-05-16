#!/usr/bin/evn python

import subprocess
import optparse

def get_arg():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to changer Mac address")
    parser.add_option("-m", "--mac", dest="mac", help="To give your new Mac address")
    (opt,arg) =  parser.parse_args()
    if not opt.interface:
        parser.error("[-] Please specify a interface, use --help for more info.")
    elif not opt.mac:
        parser.error("[-] Please specify a new mac, use -- help for more info.")
    return opt

def change_mac(interface, mac):
    print("[+] Changing the Mac address " + interface + " to " + mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])

opt = get_arg()
change_mac(opt.interface, opt.mac)

print("...................................................................\n")
iface_result = subprocess.call(["ifconfig", opt.interface])



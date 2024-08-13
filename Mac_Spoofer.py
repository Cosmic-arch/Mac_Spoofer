
#!/usr/bin/env python

import subprocess
import re
import optparse
import random
import os
import sys
import time
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("[!] Starting : ")
time.sleep(10. / 100)
os.system('clear')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0. / 100)
slowprint('''\033[1;31m \033[91m    
       __  ___                 ________                               
      /  |/  /___ ______      / ____/ /_  ____ _____  ____ ____  _____
     / /|_/ / __ `/ ___/_____/ /   / __ \/ __ `/ __ \/ __ `/ _ \/ ___/
    / /  / / /_/ / /__/_____/ /___/ / / / /_/ / / / / /_/ /  __/ /    
   /_/  /_/\__,_/\___/      \____/_/ /_/\__,_/_/ /_/\__, /\___/_/     
                                                   /____/\033[97m             
''')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)
slowprint("\t\t                                         \033[93mBy :Jashwanth\033[97m")


print("\n")
print("1. To Know your current MAC  : ")
print("2. For custom MAC changing   : ")
print("3. For Random MAC changing   : ")
print("4. Exit                      : \n")
select = int(input("Select one number            : "))

if select == 1:
	Connection_type = input("Enter your connection type      :")
	if Connection_type == "lo" :
		print("[-] Please enter correct interface i.e..wlano, eth0 and not localhost.")
		exit()
	if Connection_type == "eth0" or "eno1":
		def get_current_mac(interface):
			Result = subprocess.check_output(["ifconfig", interface])
			Result = Result.decode("utf-8")
			Current_mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", Result)
			if Current_mac_search:
				return Current_mac_search.group(0)
			else:
				print("[-] Could not read MAC from your interface. Please check your interface and re-enter it.")
		current_mac = get_current_mac(Connection_type)
		print("[+] Current MAC of", Connection_type, "is ====>", current_mac)
	elif Connection_type == "wlan0" or "wlo1":
		def get_current_mac(interface):
			Result = subprocess.check_output(["ifconfig", interface])
			Result = Result.decode("utf-8")
			Current_mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", Result)
			if Current_mac_search:
				return Current_mac_search.group(0)
			else:
				print("[-] Could not read MAC from your interface. Please check your interface and re-enter it.")
		current_mac = get_current_mac(Connection_type)
		print("[+] Current MAC of", Connection_type, "is ====>", current_mac)
if select == 2:
	connection_type = input("Enter your connectin type : ")
	Custom_mac = input("Enter your desired MAC address : ")
	print("\n")
	if connection_type == "lo":
		print("[-] Please enter correct interface i.e..wlano, eth0 and not localhost.")
		exit()
	elif connection_type == "eth0" or "eno1" :
		def get_current_mac(interface):
			Result = subprocess.check_output(["ifconfig", interface])
			Result = Result.decode("utf-8")
			Mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", Result)
			if Mac_search:
				return Mac_search.group(0)
			else:
				print("[-] Could not read your interface MAC, please enter correct one.")
		current_mac = get_current_mac(connection_type)
		print("[+] Current MAC of ", connection_type, "is ====>", current_mac)

		def change_mac(interface, mac):
			subprocess.call(["ifconfig", interface, "down"])
			subprocess.call(["ifconfig", interface, "hw", "ether", mac])
			subprocess.call(["ifconfig", interface, "up"])
			print("[+] Successfully changed the MAC address for", interface, "to =====>", mac)
		change_mac(connection_type, Custom_mac)
	elif connection_type == "wlan0" or "wlo1" :
		def get_current_mac(interface):
			Result = subprocess.check_output(["ifconfig", interface])
			Result = Result.decode("utf-8")
			Mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", Result)
			if Mac_search:
				return Mac_search.group(0)
			else:
				print("[-] Could not read your interface MAC, please enter correct one.")
		current_mac = get_current_mac(connection_type)
		print("[+] Current MAC of ", connection_type, "is ====>", current_mac)

		def change_mac(interface, mac):
			subprocess.call(["ifconfig", interface, "down"])
			subprocess.call(["ifconfig", interface, "hw", "ether", mac])
			subprocess.call(["ifconfig", interface, "up"])
			print("[+] Successfully changed the MAC address for", interface, "to =====>", mac)
		change_mac(connection_type, Custom_mac)

if select == 3:
	Random_mac= [0x00,
		   		random.randint(0x00, 0x7f),
		   		random.randint(0x00, 0x7f),
		   		random.randint(0x00, 0x7f),
		   		random.randint(0x00, 0xff),
		   		random.randint(0x00, 0xff)]
	random_mac = ':'.join(map(lambda x: "%02x" % x, Random_mac))
	connection_type = input("Enter your connectin type : ")
	print("\n")
	if connection_type == "lo":
		print("[-] Please enter correct interface i.e..wlano, eth0 and not localhost.")
		exit()
	elif connection_type == "eth0" or "eno1":
		def get_current_mac(interface):
			Result = subprocess.check_output(["ifconfig", interface])
			Result = Result.decode("utf-8")
			Mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", Result)
			if Mac_search:
				return Mac_search.group(0)
			else:
				print("[-] Could not read your interface MAC, please enter correct one.")
		current_mac = get_current_mac(connection_type)
		print("[+] Current MAC of ", connection_type, "is ====>", current_mac)

		def change_mac(interface, mac):
			subprocess.call(["ifconfig", interface, "down"])
			subprocess.call(["ifconfig", interface, "hw", "ether", mac])
			subprocess.call(["ifconfig", interface, "up"])
			print("Successfully changed the MAC address for", interface, "to ====>", mac)
		change_mac(connection_type, random_mac)
	elif connection_type == "wlan0" or "wlo1":
		def get_current_mac(interface):
			Result = subprocess.check_output(["ifconfig", interface])
			Result = Result.decode("utf-8")
			Mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", Result)
			if Mac_search:
				return Mac_search.group(0)
			else:
				print("[-] Could not read your interface MAC, please enter correct one.")
		current_mac = get_current_mac(connection_type)
		print("[+] Current MAC of ", connection_type, "is ====>", current_mac)
		def change_mac(interface, mac):
			subprocess.call(["ifconfig", interface, "down"])
			subprocess.call(["ifconfig", interface, "hw", "ether", mac])
			subprocess.call(["ifconfig", interface, "up"])
			print("[+] Successfully changed the MAC address for", connection_type, "to =====>", mac)
		change_mac(connection_type, random_mac)

if select == 4 :
	print("Have a nice day!")
	exit()

"""
This is the main file, duh. This is where you can find the all-in-one, super cool, and furiously fast Roku Troller!
Yay!!!
Ok, allow me to explain how this works.

This is a program that makes (all/mostly/maybe just one) device(s) that are accessible by the python-roku module do anything you make them do!

Let's start with the imports and what they do:

Roku - allows python to interface with Roku.
Re - allows you to search through all the junk that comes from the Roku.discover() method.
time - Kind of pointless unless you add threading. I was planning on doing that but got kind of lazy.
------------------------------------------------
Let's talk about the functions because I do not feel like properly documenting the code:

get_roku_devices - attempts to grab all Roku devices on your local network and appends them to a list.
begin_session - goes through one device at a time and does the desired action, current action will make the Roku device scroll up a little.
------------------------------------------------
Exciting! Ok, how about you edit the begin_session() function? Make sure to edit only what's below the comment!
To find out what methods you can use to interface with the Roku devices, go to the very bottom and comment out the two functions and replace them with print(roku.commands)

"""

from roku import Roku
import re
import time


available_devices = []

def get_roku_devices():
	# 
	global available_devices
	while available_devices == []:
		available_devices = Roku.discover()
	print(available_devices)


def begin_session(ip):
	roku = Roku(ip)
	#edit code below!
	for i in range(1,30):
		time.sleep(0.5)
		roku.up()
	print(f"{ip} : device messed with!")



def mess_with_devices(device_list):
	for ip in available_devices:
		address = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',str(ip)).group(0)
		begin_session(address)

get_roku_devices()
mess_with_devices(available_devices)

#!/usr/bin/env python3
import os
import pingTracker
from time import strftime

#Set all variables here
API = "o.fdUi5rBICoNHmCf02ANsN5evuPvmZJDv"

def summary():
	MSG = ""	

def pushMsg():
	MSG = "You have recieved a package at %s on %s" % \
		(strftime("%I:%M %p"), strftime("%A"))
	osCMD = "sh PingPush.sh '%s' '%s'" % (API, MSG)

	os.system(osCMD)
	

#TODO: Save how many and at what time each package arrived
#TODO: After 5 packages delivered, send logistic summary notification


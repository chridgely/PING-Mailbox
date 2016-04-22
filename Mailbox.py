#!/usr/bin/env python3
import os
import pingTracker
from time import strftime


#Set all variables here
API = "o.fdUi5rBICoNHmCf02ANsN5evuPvmZJDv"
pingTrack = pingTracker.pingTracker()

def addToDayCounter( dayArgs):
	if dayArgs == "Monday":
		pingTrack.addToMonday()
	if dayArgs == "Tuesday":
		pingTrack.addToTuesday()
	if dayArgs == "Wednesday":
		pingTrack.addToWednesday()
	if dayArgs == "Thursday":
		pingTrack.addToThursday()
	if dayArgs == "Friday":
		pingTrack.addToThursday()
	if dayArgs == "Saturday":
		pingTrack.addToSaturday()
	if dayArgs == "Sunday":
		pingTrack.addToSunday()

def pushSummary():
	TTL = "Mailbox Alert: Delivery Summary"
	MSG = pingTrack.statMostDay()	
	osCMD = "sh /home/pi/PING-Mailbox/PingPush.sh '%s' '%s' '%s'" % (API, TTL, MSG)
	os.system(osCMD)

	pingTrack.resetStats()

def pushMsg():
	time = strftime("%I:%M %p")
	day = strftime("%A")

	TTL = "Mailbox Alert: You have recieved a package"
	MSG = "You have recieved a package at %s on %s" % (time, day)
	osCMD = "sh /home/pi/PING-Mailbox/PingPush.sh '%s' '%s' '%s'" % (API,TTL, MSG)
	os.system(osCMD)
	
	addToDayCounter(day)
		
		

#TODO: Save how many and at what time each package arrived
#TODO: After 5 packages delivered, send logistic summary notification


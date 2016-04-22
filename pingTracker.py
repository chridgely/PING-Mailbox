#! /usr/bin/env python3
#Keep track of all data for analytics
import os

class pingTracker(object):
	#Python Dictionary used to record the statistics per day
	monday = 0
	tuesday = 0
	wednesday = 0
	thursday = 0
	friday = 0
	saturday = 0
	sunday = 0

	#Following code will increment each day count by 1
	def addToSunday(self):
		pingTracker.sunday += 1
	
	def addToMonday(self):
		pingTracker.monday += 1
	
	def addToTuesday(self):
		pingTracker.tuesday += 1
	
	def addToWednesday(self):
		pingTracker.wednesday += 1
	 
	def addToThursday(self):
		pingTracker.thursday += 1
	
	def addToFriday(self):
		pingTracker.friday += 1
	
	def addToSaturday(self):
		pingTrackersaturday += 1
	
	#Reset day stats to zero
	#To be called after summary msg is pushed
	def resetStats(self):
		pingTracker.monday = 0
		pingTracker.tuesday = 0
		pingTracker.wednesday = 0
		pingTracker.thursday = 0
		pingTracker.friday = 0
		pingTracker.saturday = 0
		pingTracker.sunday = 0
	
	def statMostDay(self):
		mostDay = " "
		mostNum = 0
	
		if pingTracker.monday > mostNum:
			mostNum = pingTracker.monday
			mostDay = "Monday"
		if pingTracker.tuesday > mostNum:
			mostNum = pingTracker.tuesday
			mostDay = "Tuesday"
		if pingTracker.wednesday > mostNum:
			mostNum = pingTracker.wednesday
			mostDay = "Wednesday"
		if pingTracker.thursday > mostNum:
			mostNum = pingTracker.thursday
			mostDay = "Thursday"
		if pingTracker.friday > mostNum:
			mostNum = pingTracker.friday
			mostDay = "Friday"
		if pingTracker.saturday > mostNum:
			mostNum = pingTracker.saturday
			mostDay = "Saturday"
		if pingTracker.sunday > mostNum:
			mostNum = pingTracker.sunday
			mostDay = "Sunday"
	
		#Linguistical Sysntax is important too!!!
		if mostNum > 1: 
			return "You have recieved the majority of your packages on %s, a total of %d packages" % (mostDay, mostNum)
		else:
			return 	"Of your most recent recieved packages, you have recieved them each on different days"
	

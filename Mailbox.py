#!/usr/bin/env python3
from pushbullet import Pushbullet
from time import strftime

#Set all variables here
pb = Pushbullet("o.YZqCGqReW0YkjrA7iPJCenRJUIpUPAMM")
title = "Mailbox Alert"

def pushMsg():
	#Set time
	time = strftime ("%a %I:%M%p")
	msg = "You have received a package on %s" %(time)	

        #Clear any previous push notifications
        #Pushbullet will resend if not done
        pushes = pb.get_pushes()
       # if pushes:
        latest = pushes[0]
        pb.dismiss_push(latest.get("iden"))
        pb.delete_push(latest.get("iden"))

        #Push notification to all devices connected to key
        push = pb.push_note(title, msg)

#TODO: Save how many and at what time each package arrived
#TODO: After 5 packages delivered, send logistic summary notification
#TODO: Implement this script into execution loop, activated when laser tripped


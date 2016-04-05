#! /usr/bin/env python3

#Sensor test program

import spidev
from Mailbox import pushMsg
from time import sleep

#Variables
tol = 30
package = False

#Establish SPI device on Bus 0, Device 0
spi = spidev.SpiDev()
spi.open(0,0)

def getAdc (channel):
	#check valid
	if ((channel>7) or (channel<0)):
		return -1

	#SPI Transaction
	r = spi.xfer([1, (8+channel) << 4, 0])

	#Filter data bits from return bits
	adcOut = ((r[1]&3) << 8) + r[2]
	percent = int(round(adcOut/10.24))
	
	#print out 0-1023 value and percentage
	print("ADC Output: {0:4d}	Percentage: {1:3}%".format (adcOut,percent))
	sleep(5)
	return percent

while True:
	if getAdc(0) > 30:
		if package == False:
			package = True
			pushMsg()
	else:
		package = False 
	

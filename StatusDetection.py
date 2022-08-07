#!/usr/bin/python

import RPi.GPIO as GPIO
import os, time

GPIO.setmode(GPIO.BCM)

print ("Activating pin 20 to enable Power-Management-HAT shutddown.")
GPIO.setup(20, GPIO.IN)

print ("Telling Power-Management-HAT that Raspberry Pi is running by setting pin21 to High.")
GPIO.setup (21, GPIO.OUT)
GPIO.output(21, GPIO.HIGH)

while True:
	if (GPIO.input(20)):
		print ("Power-Management-HAT signaled a shutdown request by setting pin20 to High.")
		os.system("sudo shutdown -h 120 \"Poser-Management-HAT initiated a system shutdown.\"")
		break
	time.sleep(2.0)

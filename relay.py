#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
# Set all pins as output
GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)

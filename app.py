#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
while True:
    GPIO.output(12, True)
    GPIO.output(11, True)
    print("LED is ON ok!! foo")
    time.sleep(8)
    GPIO.output(12, False)
    GPIO.output(11, False)
    print("LED is OFF ok!! baa")
    time.sleep(8)

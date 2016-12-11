#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
while True:
    GPIO.output(2, True)
    print("on")
    time.sleep(2)
    GPIO.output(2, False)
    time.sleep(2)
    print("off")

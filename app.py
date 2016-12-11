#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.OUT)
while True:
    GPIO.output(14, True)
    print("on")
    time.sleep(2)
    GPIO.output(14, False)
    time.sleep(2)
    print("off")

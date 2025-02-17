#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import commands

count = 2
print("APP Started")
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
while True:
    GPIO.output(12, True)
    GPIO.output(11, True)
    print("LED is ON")
    time.sleep(count)
    GPIO.output(12, False)
    GPIO.output(11, False)
    print("LED is OFF")
    time.sleep(count)
    print("")
    print(str(commands.getoutput("systemctl status isaax-agent")))
    print("")
    print("___________")
    print("")
    print(str(commands.getoutput("ps aux | grep isaax")))
    print("")

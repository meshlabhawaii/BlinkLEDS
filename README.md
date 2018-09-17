# BlinkLEDS
OCN418 blinking blinking
Code repository for each of your LED exercises

import time 
import RPi.GPIO as GPIO
from random import randint

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)


pin=1

while True:
    for i in range (100):
        interval=i/100
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)
        time.sleep(interval)
        GPIO.output(4,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.LOW)
        time.sleep(interval)
        GPIO.output(4,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.HIGH)
        time.sleep(interval)
    
    





GPIO.cleanup(4)

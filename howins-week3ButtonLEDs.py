import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5,GPIO.OUT)

x=0


# This code changes the two LEDs that are lit up between clicks

while True:
    if not GPIO.input(21):
        x=x+1
       
        
        if x == 1:
            GPIO.output(12, GPIO.HIGH)
            GPIO.output(4, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            
        if x == 2:
            GPIO.output(12, GPIO.HIGH)
            GPIO.output(4, GPIO.LOW)
            GPIO.output(5, GPIO.HIGH)
            
        
        if x == 3:
            GPIO.output(12, GPIO.LOW)
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(4, GPIO.HIGH)
            x=0
            

    
    while not GPIO.input(21):
        pass
  
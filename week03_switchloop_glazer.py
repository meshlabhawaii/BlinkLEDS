import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

counter = 0
GPIO.output(20,GPIO.LOW)
GPIO.output(26,GPIO.LOW)
GPIO.output(12,GPIO.LOW)

while True:
    if not GPIO.input(17):
        if counter == 0:
            GPIO.output(20,GPIO.LOW)
            GPIO.output(26,GPIO.LOW)
            GPIO.output(12,GPIO.LOW)
            print('zero')
        while not GPIO.input(17):
            pass
            
        counter = counter + 1
        print(counter)

        if counter == 1:
            GPIO.output(20,GPIO.HIGH)
            GPIO.output(26,GPIO.LOW)
            GPIO.output(12,GPIO.LOW)
            print('one')
        while not GPIO.input(17):
            pass
            
        if counter == 2:
            GPIO.output(20,GPIO.LOW)
            GPIO.output(26,GPIO.HIGH)
            GPIO.output(12,GPIO.LOW)
            print('two')
        while not GPIO.input(17):
            pass

        if counter == 3:
            GPIO.output(20,GPIO.LOW)
            GPIO.output(26,GPIO.LOW)
            GPIO.output(12,GPIO.HIGH)
            print('three')
        while not GPIO.input(17):
            pass

        if counter >= 3:
            counter = 0
            

    

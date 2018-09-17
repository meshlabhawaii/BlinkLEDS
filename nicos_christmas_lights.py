import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

for i in range (0,9001):
    interval=(i%20)/80
    
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.HIGH)
    
    time.sleep(interval)
    
    GPIO.output(4, GPIO.HIGH)
    GPIO.output(6, GPIO.LOW)
    
    time.sleep(interval)
    
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    
    time.sleep(interval)

GPIO.cleanup(4)
GPIO.cleanup(5)
GPIO.cleanup(6)

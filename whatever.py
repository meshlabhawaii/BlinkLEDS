import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

pin1 = 4
pin2 = 10
interval = 0.1

while True:
    GPIO.output(pin1, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(pin2, GPIO.LOW)
    time.sleep(4*interval)

    GPIO.output(pin1, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(pin2, GPIO.LOW)
    time.sleep(4*interval)






GPIO.cleanup(4)




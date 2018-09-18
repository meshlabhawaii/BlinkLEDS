import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

drseuss = .01
interval = .05

oahu = .2
mango = .1


while True:
    print('s')
    for i in range(5):
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)

        time.sleep(drseuss)

        GPIO.output(4, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)

        time.sleep(interval)

        
    print('o')
    for i in range(5):
        GPIO.output(4, GPIO.LOW)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)

        time.sleep(oahu)
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)

        time.sleep(mango)

    print('s')
    for i in range(5):
        GPIO.output(4, GPIO.LOW)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(17, GPIO.LOW)

        time.sleep(drseuss)

        GPIO.output(4, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)

        time.sleep(interval)



GPIO.cleanup(4

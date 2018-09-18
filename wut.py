import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)


counter = 0


interval = 0.1


while True:
    if not GPIO.input(26):
        counter = counter + 1
        print(counter)

        if counter == 1:
            GPIO.output(4, GPIO.HIGH)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            print('one')
        if counter == 2:
            GPIO.output(4, GPIO.LOW)
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            print('two')
        if counter == 3:
            GPIO.output(4, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(25, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            print('three')
        if counter == 4:
            GPIO.output(4, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(17, GPIO.LOW)
            print('four')
        if counter == 5:
            GPIO.output(4, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            print('five')
            
            counter = 0


    
    while not GPIO.input(26):
        time.sleep(0.01)
        

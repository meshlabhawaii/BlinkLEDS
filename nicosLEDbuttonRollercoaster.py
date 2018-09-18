import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.output(5, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(20, GPIO.LOW)
counter = 0
ledCounter = 0
status = 0
up = True
while True:
    if not GPIO.input(4):
        if status != 1:
            if up:
                ledCounter += 1
                if ledCounter == 6:
                    ledCounter = 4
                    up = False
            else:
                ledCounter -= 1
                if ledCounter == -1:
                    ledCounter = 1
                    up = True
            if ledCounter == 0:
                GPIO.output(5, GPIO.LOW)
            if ledCounter == 1:
                if up:
                    GPIO.output(5, GPIO.HIGH)
                else:
                    GPIO.output(6, GPIO.LOW)
            if ledCounter == 2:
                if up:
                    GPIO.output(6, GPIO.HIGH)
                else:
                    GPIO.output(21, GPIO.LOW)
            if ledCounter == 3:
                if up:
                    GPIO.output(21, GPIO.HIGH)
                else:
                    GPIO.output(20, GPIO.LOW)
            if ledCounter == 4:
                if up:
                    GPIO.output(20, GPIO.HIGH)
                else:
                    GPIO.output(16, GPIO.LOW)
            if ledCounter == 5:
                GPIO.output(16, GPIO.HIGH)
                    
            counter += 1
            
            print(counter)
        status = 1
    else:
        status = 0
    time.sleep(0.01)    

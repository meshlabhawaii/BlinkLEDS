GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

counter = 0

#initialize the LEDs so that ONE LED is lit at the beginning

while True:
    if not GPIO.input(23):
        counter = counter + 1
        print(counter)

        if counter == 1:
            GPIO.output(4, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            print('maythe')
        if counter == 2:
            GPIO.output(4, GPIO.LOW)
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            print('force')
        if counter == 3:
            GPIO.output(4, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            print('bewithyou')
        if counter == 4:
            GPIO.output(4, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(25, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            print('luke')
        if counter == 5:
            GPIO.output(4, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)
            print('Iamyourfather')
            counter = 0
        

        while not GPIO.input(23):
            pass
            


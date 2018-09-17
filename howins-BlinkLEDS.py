import time
import RPi.GPIO as GPIO

# within the RPi GPIO Library Set the mode to GPIO.BCM

GPIO.setmode(GPIO.BCM)

# Set up GPIO 4 as an output
# GPIO 4 says "ET PHONE HOME"
# GPIO 5 says "THESE AREN'T THE DROIDS YOU'RE LOOKING FOR"
# GPIO 21 says "THESE AREN'T THE DROIDS WE'RE LOOKING FOR"

GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

dot=0.25
dash=0.5

# this is the part that controls the pin
while True:
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dash)
     
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dash)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dash)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dash)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dash)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dash)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep (dash)

# -----------------------------


    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)
    
    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)
    
    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dash)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(5, GPIO.LOW)
    time.sleep (dot)


    
    
    
    # ------------------------




# to repeat over acertain interval:
# for i in range(3):
# stuff here will be repeated 3 times
# indenting with while true loop goes forever
# If you want to send SOS, While true: for i in range (3) then make long interval
# follow that with i in range (3) then short interval



GPIO.cleanup(4)
GPIO.cleanup(5)




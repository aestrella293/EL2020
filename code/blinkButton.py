#Import libraries
import RPi.GPIO as GPIO
import time
import signal
import os

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Define the function that will toggle the state of the light
def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(.1)
	GPIO.output(pin,False)
	time.sleep(.1)

#Use the blinkOnce function ina loopity-loop when the button is pressed
try:
	while True:
		input_state = GPIO.input(26)
		if input_state==False:
			for i in range (15):
				blinkOnce(17)
			time.sleep(0.2)

except KeyboardInterrupt:
	os.system('clear')
	print ("Thanks for blinking and thinking!")
	GPIO.cleanup()

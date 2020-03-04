#Import Libraries we will be using
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import os

#assign GPIO pins
tempPin = 27
redPin = 17
buttonPin = 26

#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT11

#LED Variables================================================
#Duration of each blink
blinkDur = .1
#Number of times to Blink the LED
blinkTime = 7
#=============================================================
#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print ('This code is running')
def oneBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin, False)
	time.sleep(blinkDur)
def readF(tempPin):
	humidity, temperature =  Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 + 32
	if humidity != 0 and temperature != 0:
		tempFahr = '{0:0.1f} * F' .format(temperature)
	else:
		print ('Error Reading the Sensor')
	return tempFahr
try:

	while True:
		input_state = GPIO.input(buttonPin)
		if  input_state == False:
			for i in range (blinkTime):
				oneBlink(redPin)
			time.sleep(.2)
			data = readF(tempPin)
			print (data)
except KeyboardInterrupt:
	os.system('clear')
	print ('Thanks for Blinking and Thinking')
	GPIO.cleanup()

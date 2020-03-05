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

#Use the blinkOnce function in a loop when the button is pressed
try:
	with open("log/tempLog.csv" , "a") as log:
		while True:
			input_state = GPIO.input(buttonPin)
			if input_state == False:
				for i in range (blinkTime):
					oneBlink(redPin)
				time.sleep(.2)
				data1 = readF(tempPin)
				#data2 = readH(tempPin)
				print ('The Temperature is ' + data1)
				#print ('The Humidity is ' + data2)
				log.write("{0},{1}\n".format(time.strftime ("%Y -%m -%d %H:%M:%S"),str(data1))) #, str(data2)))
				log.flush()
				os.fsync(log)

except KeyboardInterrupt:
	os.system('clear')
	print ('Thanks for Blinking and Thinking')
	GPIO.cleanup()

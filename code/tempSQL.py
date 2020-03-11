#Import Libraries we will be using
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import os
import sqlite3 as sql
import sys

#assign GPIO pins
tempPin = 27
redPin = 17
greenPin = 22
buttonPin = 26

#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT11

#LED Variables================================================
#Duration of each blink
blinkDur = .1
#Number of times to Blink the LED
blinkTime = 7
#=============================================================
#STMP email variables
#eFROM = "aestrella293@gmail.com"
#eTO =
#subject = "Alert 1"

#Connnect to Database
con = sql.connect ('../log/tempLog.db')
cur = con.cursor()

#set the initial checkbit to 0. This will throw a warning when run, but will work just fine
eChk = 0

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)

#GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print ('This code is running')

def oneBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin, False)
	time.sleep(blinkDur)

def alert(tempF):
	global eChk
	if eChk == 0:
		Text = "The monitr temp is now: " + str(tempF)

def readDH11(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5 +32

	if humidity != 0 and temperature != 0:
		tempFahr = '{0:0.1f}' .format(temperature)
		tempHumid = '{1:0.1f}' .format(temperature, humidity)
	else:
		print ('Error Reading the Sensor')
	return tempFahr, tempHumid

#Read Temp initially
oldTime = 60
tempFahr, tempHumid = readDH11(tempPin)

#Use the blinkOnce function in a loop when the button is pressed
try:
	while True:
		if 68 <= float(tempFahr) <= 78:
			eChk = 0
			GPIO.output(redPin, False)
			GPIO.output(greenPin, True)
		else:
			GPIO.output(greenPin, False)
			alert(tempFahr)
			oneBlink(redPin)

		if time.time() - oldTime > 59:
			tempFahr, Humid = readDH11(tempPin)
			print (tempFahr, Humid)
			#Defines and execurtes the sql query
			cur.execute('INSERT INTO tempLog values(?,?,?)',(time.strftime ("%Y-%m-%d %H:%M:%S "), tempFahr, tempHumid))
			con.commit()

			table = con.execute("select * from tempLog")
			os.system('clear')
			print "%-30s %-20s %-20s" %("Date/Time", "Temp (F)", "Humidity(%)")
			for row in table:
				print "%-30s %-20s %-20s" %(row[0], row[1], row[2])
			oldTime = time.time()

except KeyboardInterrupt:
	os.system('clear')
	print ('Thanks for Blinking and Thinking')
	GPIO.cleanup()

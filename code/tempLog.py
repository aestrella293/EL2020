import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import os
import sqlite3 as sql
import smtplib

redPin = 17
tempPin = 27
buttonPin = 22

tempSensor = Adafruit_DHT.DHT11

blinkDur = 0.1
blinkTime = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(tempPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

con = sql.connect('../log/tempLog.db')
cur = con.cursor()

def readF(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}'.format(temperature)
		print(tempFahr)
	else:
		print('Error Reading Sensor')
	return tempFahr

def readH(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	if humidity is not None and temperature is not None:
		humid = '{0:0.1f}'.format(humidity)
		print(humid)
	else:
		print('Error Reading Sensor')
	return humid

print('is running')
try:

#	with open("../log/tempLog.csv", "a") as log:

		while True:
			dataT = readF(tempPin)
			dataH = readH(tempPin)
			cur.execute('INSERT INTO templog values(?,?,?)',(time.strftime('%Y-%m-%d %H:%M:%S'), dataT, dataH))
			con.commit()
			table = con.execute("select * from tempLog")
			time.sleep(60)
			os.system('clear')

except KeyboardInterrupt:
	os.system('clear')
	print('Thanks for Blinking and Thinking!')
	GPIO.cleanup()

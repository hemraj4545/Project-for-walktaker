import RPi.GPIO as GPIO

inputPin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputPin,GPIO.IN)

while True:
	print(GPIO.input(inputPin))

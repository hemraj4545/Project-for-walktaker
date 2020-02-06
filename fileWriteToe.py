from datetime import datetime
import time
import RPi.GPIO as GPIO

toePin=3

dataFile=open('dataTimeToe.csv','a+')
prevTime=datetime.now().minute*60+datetime.now().second+datetime.now().microsecond*0.000001

GPIO.setmode(GPIO.BCM)
GPIO.setup(toePin,GPIO.IN)


while True:
	if GPIO.input(toePin)==0:
		print('Read')
		time.sleep(0.5)
		nowTime=datetime.now().minute*60+datetime.now().second+datetime.now().microsecond*0.000001
		diffTime=nowTime-prevTime
		prevTime=nowTime
		dataFile.write(str(diffTime)+'\n')

f.close()

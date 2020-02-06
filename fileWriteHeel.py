from datetime import datetime
import time
import RPi.GPIO as GPIO

heelPin=2

dataFile=open('dataTimeHeel.csv','a+')
prevTime=datetime.now().minute*60+datetime.now().second+datetime.now().microsecond*0.000001

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.IN)


while True:
	if GPIO.input(heelPin)==0:
		time.sleep(0.5)
		print('READ')
		nowTime=datetime.now().minute*60+datetime.now().second+datetime.now().microsecond*0.000001
		diffTime=nowTime-prevTime
		prevTime=nowTime
		dataFile.write(str(diffTime)+'\n')

f.close()


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

print("GPIO pulse")

def pulse(pin_nr, high_time, low_time, time3, time4):
	#GPIO.output(led,GPIO.HIGH)
	#time.sleep(high_time)
	#GPIO.output(led,GPIO.LOW)
	#time.sleep(low_time)
	#GPIO.output(led,GPIO.HIGH)
	#time.sleep(time4)
	#GPIO.output(led,GPIO.LOW)
	#time.sleep(low_time)
	GPIO.output(led,GPIO.HIGH)
	time.sleep(high_time)
	GPIO.output(led,GPIO.LOW)
	time.sleep(low_time)
	GPIO.output(led,GPIO.HIGH)
	time.sleep(high_time)
	GPIO.output(led,GPIO.LOW)
	time.sleep(low_time)
	GPIO.output(led,GPIO.HIGH)
	time.sleep(high_time)
	GPIO.output(led,GPIO.LOW)
	time.sleep(low_time)
	GPIO.output(led,GPIO.HIGH)
	time.sleep(high_time)
	GPIO.output(led,GPIO.LOW)
	time.sleep(low_time)
	GPIO.output(led,GPIO.HIGH)
	time.sleep(time4)
	GPIO.output(led,GPIO.LOW)
	time.sleep(low_time)
	
	
led =18		
GPIO.setup(led, GPIO.OUT)
while True:
	pulse(led,0.2,0.2, 0.2, 5)

import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "sr04 print" )

sr04_trig = 20
sr04_echo = 21

GPIO.setup( sr04_trig, GPIO.OUT )
GPIO.setup( sr04_echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )

def sr04( trig_pin, echo_pin ):
   """
   Return the distance in cm as measured by an SR04
   that is connected to the trig_pin and the echo_pin.
   These pins must have been configured as output and input.s
   """
    
   # send trigger pulse
   # inplement this step
   GPIO.output(sr04_trig, True)
   time.sleep(0.00001)
   GPIO.output(sr04_trig,False)
   
   # wait for echo high and remember its start time
   # inplement this step
   begintijd = time.time()
   eindtijd = time.time()
   
   # wait for echo low and remember its end time
   # inplement this step
   while GPIO.input(sr04_echo) == 0:
       begintijd = time.time()
       
   while GPIO.input(sr04_echo) == 1:
       eindtijd = time.time()
       
   duur = eindtijd - begintijd
   afstand = (duur * 34300) /2
   
   # calculate and return distance
   # inplement this step
   return afstand

while True:
   print( sr04( sr04_trig, sr04_echo ))
   time.sleep( 0.5 )



 
import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "input copy" )

led = 18
switch = 23
switch2 = 24

GPIO.setup( led, GPIO.OUT )
GPIO.setup( switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
GPIO.setup( switch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
while True:
   if( GPIO.input( switch ) ):
      GPIO.output( led, GPIO.HIGH )
   elif(GPIO.input(switch2)):
      GPIO.output( led, GPIO.LOW )
   time.sleep( 0.1 )

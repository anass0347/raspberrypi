import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "binair walk" )

led_pins = [ 18, 4, 17, 27, 22 ]

for gpio in led_pins:
   GPIO.setup( gpio, GPIO.OUT )

def leds( pins, value, delay ):
    teller = 1
    for gpio in pins:
        if value % 2 == 1:
           GPIO.output( gpio, GPIO.LOW )
        else:
           GPIO.output( gpio, GPIO.HIGH )
           #print(teller)
           teller +=1
           if teller > 5:
               led_pins.reverse()
        value = value // 2
        print(led_pins)
    time.sleep( delay )
    
delay = 0.2
while True:
   leds( led_pins,  1, delay )
   leds( led_pins,  2, delay )
   leds( led_pins,  4, delay )
   leds( led_pins,  8, delay )
   leds( led_pins, 16, delay )
   led_pins.reverse()


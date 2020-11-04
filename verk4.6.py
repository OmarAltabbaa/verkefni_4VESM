import RPi.GPIO as GPIO
from gpiozero import LED
import time
import digitalio
import board
from Adafruit_IO import Client, Feed, RequestError

ADAFRUIT_IO_KEY = 'aio_SQqU05T6tDCSg4j32ekv5UmbPFzu'
 
# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'OmarAltabbaa'


aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: 
    analog = aio.feeds('Led')
except RequestError: 
    feed = Feed(name='Led')
    analog = aio.create_feed(feed)
    
photocell = digitalio.DigitalInOut(board.D18)
servoPIN = 17
led1 = LED(14)
p = GPIO.PWM(servoPIN, 50)
newState = 'on'
oldState = 'off'

while True:
    read = aio.receive(analog.key)
    val =  photocell.value
    newState = read.value
    print(newState)
    if oldState != newState:
       if newState == 'on' :
           led1.on()
           print(val)
           aio.send(analog.key, val)
           p.ChangeDutyCycle(7)
           sleep(1) 
       else:
           led1.off()
           print(val)
           aio.send(analog.key, val)
           p.ChangeDutyCycle(17)
           sleep(1)          
    oldState = newState
    sleep(1)
            



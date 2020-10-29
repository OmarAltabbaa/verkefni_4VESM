"""
'digital_out.py'
===================================
Example of turning on and off a LED
from the Adafruit IO Python Client
 
Author(s): Brent Rubell, Todd Treece
"""
# Import standard python modules
import time
 
# import Adafruit Blinka
import digitalio
import board
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
 
# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError
 
# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_CtbB54FpMjCJa29IpmTI9eTWR7qt'
 
# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'OmarAltabbaa'
 
# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
 
try: # if we have a 'digital' feed
    digital = aio.feeds('digital')
except RequestError: # create a digital feed
    feed = Feed(name="digital")
    digital = aio.create_feed(feed)
 
# led set up
led = digitalio.DigitalInOut(board.D5)
led.direction = digitalio.Direction.OUTPUT
 
 
while True:
    data = aio.receive(digital.key)
    if data.value == "ON":
        GPIO.output(5, GPIO.HIGH)
        sleep(2)
        print('received <- ON\n')
    elif data.value == "OFF":
        GPIO.output(5, GPIO.LOW)
        sleep(2)

        print('received <- OFF\n')
 
    # set the LED to the feed value
    led.value = data.value
    # timeout so we dont flood adafruit-io with requests
    time.sleep(0.5)

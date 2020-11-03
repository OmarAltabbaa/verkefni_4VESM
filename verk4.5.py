"""
'analog_in.py'
==================================
Example of sending analog sensor
values to an Adafruit IO feed.
Author(s): Brent Rubell
Dependencies:
    - Adafruit_Blinka
        (https://github.com/adafruit/Adafruit_Blinka)
    - Adafruit_CircuitPython_MCP3xxx
        (https://github.com/adafruit/Adafruit_CircuitPython_MCP3xxx)
"""
# Import standard python modules
import time

# import Adafruit Blinka
import board
import digitalio
import busio
import RPi.GPIO as GPIO

# import Adafruit IO REST client
from Adafruit_IO import Client, Feed, RequestError
import serial

# import Adafruit CircuitPython MCP3xxx library


# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_lIPZ92j876FGOeQw7NmIWnum33FL'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'OmarAltabbaa'
# Create an instance of the REST client
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we have a 'analog' feed
    analog = aio.feeds('analog')
except RequestError: # create a analog feed
    feed = Feed(name='analog')
    analog = aio.create_feed(feed)

ser =serial.Serial("/dev/ttyACM1",115200)

while True:
    sensor_data =int(ser.readline())

    print('Analog Data -> ', sensor_data)
    aio.send(analog.key, sensor_data)

    aio.send(analog.key,sensor_data )
    time.sleep(3)

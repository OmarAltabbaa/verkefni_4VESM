import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
 # Importing sleep from time library
from Adafruit_IO import Client, Feed, RequestError
import board
GPIO.setwarnings(False) # Ignore warning for now
import digitalio
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
from time import sleep 
# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_DHiv11wZ0MFVXGVTqlgyoKdJVqXc'
 
# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'OmarAltabbaa'

led_pin = 21
led = digitalio.DigitalInOut(board.D21)
led.direction = digitalio.Direction.OUTPUT          # Initializing the GPIO pin 21 for LED

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setup(led_pin, GPIO.OUT)   # Declaring pin 21 as output pin

pwm = GPIO.PWM(led_pin, 100)    # Created a PWM object
pwm.start(0)# Started PWM at 0% duty cycle

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
prev_read=0
try: # if we have a 'digital' feed
    digital = aio.feeds('omar')
except RequestError: # create a digital feed
    feed = Feed(name="omar")
    digital = aio.create_feed(feed)

def map_range(x, in_min, in_max, out_min, out_max):
    """re-maps a number from one range to another."""
    mapped = (x-in_min) * (out_max - out_min) / (in_max-in_min) + out_min
    if out_min <= out_max:
        return max(min(mapped, out_max), out_min)
    return min(max(mapped, out_max), out_min)

while True:
    # grab the `analog` feed value
    digital_read = aio.receive(digital.key)
    if digital_read.value != prev_read:
        print('received <- ', digital_read.value)
        # map the analog value from 0 - 1023 to 0 - 65534
        digital_value = map_range(int(digital_read.value), 0, 1024, 0, 100)
        # set the LED to the mapped feed value
        print(int(digital_value))
        pwm.ChangeDutyCycle(int(digital_value))
    prev_read = digital_read.value
    # timeout so we don't flood IO with requests
    sleep(2)
pwm.stop() 
GPIO.cleanup()  # Make all the output pins LOW

from gpiozero import Button
from time import sleep
from Adafruit_IO import Client
import digitalio

ADAFRUIT_IO_KEY = 'aio_zgfb79f8EKTY5yQ1udl8fe7tqyvB'
 

ADAFRUIT_IO_USERNAME = 'OmarAltabbaa'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

button = Button(17)
pi_button = aio.feeds('om')
while True:
    if button.is_pressed:
        aio.send(pi_button.key, 1)
        print("Pressed")
    else:
        aio.send(pi_button.key, 0)
        print("Released")
    sleep(5)

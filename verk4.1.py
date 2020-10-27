from gpiozero import Button
from time import sleep
from Adafruit_IO import Client
import digitalio

ADAFRUIT_IO_KEY = 'aio_vPxq54z6xnv2POrNrVXasw4wcIe6'
 

ADAFRUIT_IO_USERNAME = 'OmarAltabbaa'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

button = Button(17)
pi_button = aio.feeds('button')
while True:
    if button.is_pressed:
        aio.send(pi_button.key, 1)
        print("Pressed")
    else:
        aio.send(pi_button.key, 0)
        print("Released")
    sleep(2)

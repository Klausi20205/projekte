Python 3.7.3 (default, Jan 22 2021, 20:04:44) 
[GCC 8.3.0] on linux

>>> import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Relays = (14, 15, 18, 23, 24, 25, 8, 7)
GPIO.setup(Relays[i], GPIO.OUT)

GPIO.output(Relays[i], GPIO.HIGH)
print('Normally opened pin is HIGH')
GPIO.output(Relays[i], GPIO.LOW)
print('Normally opened pin is LOW')
print('Script end!')

GPIO.cleanup()

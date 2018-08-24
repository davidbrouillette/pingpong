import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)
    
def LedOn(pin):
    GPIO.output(pin, GPIO.HIGH)

def LedOff(pin):
    GPIO.output(pin, GPIO.LOW)
    
LedOff(18)
time.sleep(1)
LedOn(18)
time.sleep(1)
LedOff(18)
time.sleep(1)
LedOn(18)
time.sleep(1)
LedOff(18)
time.sleep(1)
LedOn(18)
time.sleep(1)
LedOff(18)
time.sleep(1)

while True:
    button = GPIO.input(23)
    
    if button == False:
        LedOn(18)
    else:
        LedOff(18)


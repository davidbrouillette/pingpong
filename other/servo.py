import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pwm = GPIO.PWM(12, 50)
pwm.start(5)

dutyzero = float(3)
duty180 = float(12)

while True:
    buttonPressed= GPIO.input(4)
    if buttonPressed == False:
        pwm.ChangeDutyCycle(duty180)
    else:
        pwm.ChangeDutyCycle(dutyzero)

#!/usr/bin/python
import RPi.GPIO as GPIO
from gpiozero import LED
import time

# setup pin
channel = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

led = LED(17)

def callback(channel):
        if GPIO.input(channel):
            led.on() # low sound
        else:
            led.off() # high sound

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  
GPIO.add_event_callback(channel, callback) 

while True:
        time.sleep(1)
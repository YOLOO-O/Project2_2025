#!/usr/bin/python
from gpiozero import Button
import time

channel = 21

sensor = Button(channel)

def callback():
    if sensor.is_pressed:
        print("Water Detected! YES")
    else:
        print("Water Detected! NO")

sensor.when_pressed = callback
sensor.when_released = callback

while True:
    time.sleep(1)

#!/usr/bin/env python

import OtenkiBuzzer
import time

disp   = OtenkiBuzzer.Display()
sensor = OtenkiBuzzer.Sensor()
buzzer = OtenkiBuzzer.Buzzer()
feed   = OtenkiBuzzer.Feed()

import atexit

def atexit_handler():
    buzzer.stop()
    disp.clear()

atexit.register(atexit_handler)

while True:
    distance = sensor.check()
    print(str(distance))

    if distance < 50:
        buzzer.beep()
        weather = feed.fetch()
        disp.show(weather)

    buzzer.stop()
    time.sleep(1)


#!/usr/bin/env python

import OtenkiBuzzer
import time

disp   = OtenkiBuzzer.Display()
sensor = OtenkiBuzzer.Sensor()
buzzer = OtenkiBuzzer.Buzzer()

while True:
    distance = sensor.check()
    print(str(distance))
    disp.show(str(distance))

    if distance < 50:
        buzzer.beep()

    time.sleep(1)

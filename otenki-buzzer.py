#!/usr/bin/env python

import OtenkiBuzzer
import time

disp   = OtenkiBuzzer.Display()
sensor = OtenkiBuzzer.Sensor()

while True:
    distance = sensor.check()
    print(str(distance))
    disp.show(str(distance))

    time.sleep(1)

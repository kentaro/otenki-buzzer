import time, wiringpi as pi

BUZZER_PIN = 21

class Buzzer:
    def __init__(self):
        pi.wiringPiSetupGpio()
        pi.pinMode(BUZZER_PIN, 1)
        self.stop()

    def beep(self):
        pi.digitalWrite(BUZZER_PIN, 1)
        time.sleep(1)

    def stop(self):
        pi.digitalWrite(BUZZER_PIN, 0)

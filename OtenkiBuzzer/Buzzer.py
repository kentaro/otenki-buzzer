import time, wiringpi as pi

BUZZER_PIN = 21

class Buzzer:
    def __init__(self):
        pi.wiringPiSetupGpio()
        pi.pinMode(BUZZER_PIN, 1)
        pi.digitalWrite(BUZZER_PIN, 0)

    def beep(self):
        pi.digitalWrite(BUZZER_PIN, 1)
        time.sleep(1)
        pi.digitalWrite(BUZZER_PIN, 0)

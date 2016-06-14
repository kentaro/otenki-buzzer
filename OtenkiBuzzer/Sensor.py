import time, wiringpi as pi

SPI_CH  = 0
READ_CH = 0

class Sensor(object):
    def __init__(self):
        pi.wiringPiSPISetup(SPI_CH, 1000000)

    def check(self):
        buffer = 0x6800 | (0x1800 * READ_CH)
        buffer = buffer.to_bytes(2, byteorder='big')
        pi.wiringPiSPIDataRW(SPI_CH, buffer)

        value    = (buffer[0] * 256 + buffer[1]) & 0x3ff
        volt     = value * 3.3 / 1034
        distance = self.gp2y0a21(volt)

        return distance

    def gp2y0a21(self, volt):
        if volt >= 2.25:
            length = (volt - 4.625) / -0.2375
        elif  volt < 2.25 and volt >= 1.7:
            length = (volt - 3.35) / -0.11
        elif  volt < 1.7 and volt >= 1.3:
            length = (volt - 2.9) / -0.08
        elif  volt < 1.3 and volt >= 0.9:
            length = (volt - 2.1) / -0.04
        elif  volt < 0.9 and volt >= 0.6:
            length = (volt - 1.35) / -0.015
        elif  volt < 0.6 and volt >= 0.5:
            length = (volt - 1.1) / -0.01
        elif  volt < 0.5:
            length = (volt - 0.8) / -0.005

        return length

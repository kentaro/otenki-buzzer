import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Display(object):
    def __init__(self):
        disp = Adafruit_SSD1306.SSD1306_128_64(rst=0, i2c_address=0x3C)
        disp.begin()
        self.disp = disp

    def show(self, text):
        self.disp.clear()

        width  = self.disp.width
        height = self.disp.height
        image  = Image.new('1', (width, height))
        draw   = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        draw.text((10, 10), text, font=font, fill=255)

        self.disp.image(image)
        self.disp.display()

import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Display:
    def __init__(self):
        disp = Adafruit_SSD1306.SSD1306_128_64(rst=0, i2c_address=0x3C)
        disp.begin()
        self.disp = disp
        self.clear()

    def show(self, text):
        self.clear()

        width  = self.disp.width
        height = self.disp.height
        image  = Image.new('1', (width, height))
        draw   = ImageDraw.Draw(image)
        font   = ImageFont.truetype('/usr/share/fonts/truetype/kochi/kochi-gothic.ttf', 15, encoding='unic')

        draw.text((5, 25), text, font=font, fill=255)

        self.disp.image(image)
        self.disp.display()

    def clear(self):
        self.disp.clear()
        self.disp.display()

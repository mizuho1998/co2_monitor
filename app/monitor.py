from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


class Monitor():
    def __init__(self):
        self.disp = self.createDisplay()
        self.image, self.width, self.height = self.createImage(self.disp)
        self.draw = self.createDraw(self.image, self.width, self.height)

        # Load default font.
        self.font = ImageFont.load_default()


    def createDisplay(self):
        # Create the I2C interface.
        i2c = busio.I2C(SCL, SDA)

        # Create the SSD1306 OLED class.
        # The first two parameters are the pixel width and pixel height.  Change these
        # to the right size for your display!
        disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

        # Clear display.
        disp.fill(0)
        disp.show()

        return disp


    def createImage(self, disp):
        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        width = disp.width
        height = disp.height
        image = Image.new("1", (width, height))

        return image, width, height


    def createDraw(self, image, width, height):
        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        return draw


    def display(self, co2, tem, hu, IP):
        # Draw some shapes.
        # First define some constants to allow easy resizing of shapes.
        padding = -2
        top = padding
        bottom = self.height - padding
        # Move left to right keeping track of the current x position for drawing shapes.
        x = 0

        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
       
        # Write four lines of text.
        self.draw.text((x, top + 0), "CO2: " + str(co2), font=self.font, fill=255)
        self.draw.text((x, top + 8), "temperaure: " + str(tem), font=self.font, fill=255)
        self.draw.text((x, top + 16), "humidity: " + str(hu), font=self.font, fill=255)
        self.draw.text((x, top + 25), "IP: " + IP, font=self.font, fill=255)

        # Display image.
        self.disp.image(self.image)
        self.disp.show()


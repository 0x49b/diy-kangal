import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import
import time
import random

# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000
FRAMERATE = 0.04

# Setup SPI bus using hardware SPI:
spi = board.SPI()

disp = st7735.ST7735R(spi, 
    rotation=90, 
    x_offset=0, 
    y_offset=0,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)


# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height


def display(image):
    # Scale the image to the smaller screen dimension
    image_ratio = image.width / image.height
    screen_ratio = width / height
    if screen_ratio < image_ratio:
        scaled_width = image.width * height // image.height
        scaled_height = height
    else:
        scaled_width = width
        scaled_height = image.height * width // image.width
    image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

    # Crop and center the image
    x = scaled_width // 2 - width // 2
    y = scaled_height // 2 - height // 2
    image = image.crop((x, y, x + width, y + height))

    # Display image.
    disp.image(image)

def squint():
    squint_images = ['squint-00.jpg','squint-01.jpg','squint-02.jpg','squint-03.jpg','squint-04.jpg']

    for img in squint_images:
        image = Image.open("jpg/" + img)
        display(image)
        time.sleep(FRAMERATE)
    
    time.sleep(1)

    squint_images_reverse = squint_images[::-1]

    for img in squint_images_reverse:
        image = Image.open("jpg/" + img)
        display(image)
        time.sleep(FRAMERATE)
    
    image = Image.open("jpg/face-00.jpg")
    display(image)

def angry():
    squint_images = ['angry-00.jpg','angry-01.jpg','angry-02.jpg','angry-03.jpg','angry-04.jpg']

    for img in squint_images:
        image = Image.open("jpg/" + img)
        display(image)
        time.sleep(FRAMERATE)
    
    time.sleep(10)

    squint_images_reverse = squint_images[::-1]

    for img in squint_images_reverse:
        image = Image.open("jpg/" + img)
        display(image)
        time.sleep(FRAMERATE)
    
    image = Image.open("jpg/face-00.jpg")
    display(image)

def energy():
    squint_images = ['energy-44.jpg','energy-34.jpg','energy-12.jpg','energy-13.jpg','energy-00.jpg']

    for img in squint_images:
        image = Image.open("jpg/" + img)
        display(image)
        time.sleep(FRAMERATE)

    squint_images_reverse = squint_images[::-1]

    for img in squint_images_reverse:
        image = Image.open("jpg/" + img)
        display(image)
        time.sleep(FRAMERATE)
    
def run():


    image = Image.new("RGB", (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    disp.image(image)

    image = Image.open("jpg/face-00.jpg")

    display(image)



if __name__ == "__main__":
    run()

    while True:
        time.sleep( random.randint(5, 15) )
        squint()
        time.sleep( random.randint(5, 15) )
        angry()
        time.sleep( random.randint(5, 15) )
        energy()
        energy()
        energy()
        energy()
        image = Image.open("jpg/face-00.jpg")
        display(image)


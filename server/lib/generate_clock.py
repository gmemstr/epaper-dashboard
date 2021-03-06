import time
from PIL import Image, ImageDraw, ImageFont
import os
import io


# This is assuming the display is landscape, rather than vertical.
height = 122
width = 250

font18 = ImageFont.truetype('server/assets/OpenSans-SemiBold.ttf', 20)
font64 = ImageFont.truetype('server/assets/OpenSans-Regular.ttf', 64)


def run_command():
    time_image = Image.new('1', (width, height), 255)
    time_draw = ImageDraw.Draw(time_image)

    time_draw.rectangle((0, 0, 250, 122), fill=255)
    time_draw.text((0, 0), time.strftime('%H:%M'), font=font64, fill=0)
    time_draw.text((0, 90), time.strftime('%a, %d %B (%Y)'),
                   font=font18, fill=0)

    try:
        pi_image = Image.open('server/assets/RPi-Logo-Black-SCREEN.png')
        pi_image.thumbnail((80,80))
        time_image.paste(pi_image, (180, 10), mask=pi_image)
    except Exception:
        print("")

    time_image = time_image.transpose(Image.ROTATE_180)
    img_byte_arr = io.BytesIO()
    time_image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return img_byte_arr

#!/usr/bin/python

import sys
from PIL import Image

# Remove the first argument (the script name)
sys.argv.pop(0)
print ('Converting ', len(sys.argv), 'image(s)')

for imagesList in sys.argv:
    img = Image.open(imagesList)
    img = img.convert("RGBA")
    # Create mask
    for x in range(img.height):
        for y in range(img.width):
            r, g, b, a = img.getpixel((x, y))
            if a > 0:
                img.putpixel((x, y), (0, 0, 0))
    # Add '_mask' to the filename
    img.save(imagesList[:-4] + '_mask.png', 'PNG')
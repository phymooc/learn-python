#! python3
# resizeAndAddLogo.py - Resize all images to fix in a 300x300 square, and add catlog.png to the lower-right corner

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# loop over all files
for filename in os.listdir('.'):
    if not(filename.endswith('.png') or filename.endswith('.jpg'))\
            or filename == LOGO_FILENAME:
        continue
    im = Image.open(filename)
    width, height = im.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE/width)*height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE/height)*width)
            height = SQUARE_FIT_SIZE

        print('Resizing %s...' % (filename))
        im = im.resize((width, height))
        print('adding logo to %s ...' % (filename))
        im.paste(logoIm, (width-logoWidth, height-logoHeight), logoIm)
        im.save(os.path.join('withLogo', filename))

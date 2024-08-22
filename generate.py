# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import io
from reportlab.graphics.barcode import createBarcodeImageInMemory
from PIL import Image


# https://docs.reportlab.com/reportlab/userguide/ch1_intro/
# https://docs.reportlab.com/reportlab/barcode/
# https://pillow.readthedocs.io/en/stable/
# https://docs.python.org/3/library/io.html

# Barcode Types: 
#     EAN8, EAN13, EAN5, ISBN, UPCA, QR, Code128, Code128Auto
#     Standard39, Standard93, MSI, Codebar, Code11, FIM, POSTNET
#     Extended39, Extended93, I2of5, ECC200DataMatrix


barcode = createBarcodeImageInMemory(
    'Code128',                  # Refer to barcode types 
    value='123456789012',       # code to be encoded/printed
    width=300, 
    height=60,
    format='png'                # png, gif, tiff
)

# Display and show the image
img = Image.open(io.BytesIO(barcode))
img.show()

# if you want to save it to a file
f = open('barcode.png', 'wb')
f.write(barcode)
f.close()
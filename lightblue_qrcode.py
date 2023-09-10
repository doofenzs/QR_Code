#lightblue_qrcode.py

#In this section, you’ll modify the color of the background.
# the quiet zone, and the light and dark modules of your QR codes.

import segno

qrcode = segno.make_qr("Hello World!")
qrcode.save(
    "lightblue_qrcode.png",
    scale = 5,
    light = "#ADD8E6" # ADD8E6 is is a light blue colour.
)
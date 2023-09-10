#scaled_qrcode.py

#If you’d like to to adjust the size of the QR code,
#Then you can add a scale parameter to the .save() method. 
#The scale parameter is a scaling factor that changes the width and height of the QR.

import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save(
    "scaled_qrcode.png",
    scale=5,
)    
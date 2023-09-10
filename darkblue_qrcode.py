#darkblue_qrcode.py

#You can also change the colors of all the black modules of the QR code.
#In order to do, I can set a value with a color.
#Choice in the dark parameter in the .save() method.

import segno

qrcode = segno.make_qr("Hello World!")
qrcode.save(
    "darkblue_qrcode.png",
    scale = 5,
    dark = "darkblue"
)
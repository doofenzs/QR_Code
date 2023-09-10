#borderless_qrcode.py

# To increase the scannability of the QR code and make sure.
# That devices such as smartphones can clearly access the information.
# This blank space is referred to as the quiet zone.

import segno

qrcode = segno.make_qr("Hello World!")
qrcode.save("borderless_qrcode.png",
        scale = 5,
        border = 0)
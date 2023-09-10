#wide_border_qrcode.py

# Want to increase the size of the quiet zone.
# create a wider border for your QR code.

import segno

qrcode = segno.make_qr("Hello World!")
qrcode.save(
    "wide_border_qrcode.png",
    scale = 5,
    border = 10
)
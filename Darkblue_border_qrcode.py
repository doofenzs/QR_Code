#darkblue_qrcode.py

# Could make changes in QR code image.
# Changing the color of the quiet zone by adding a quiet_zone parameter.

import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save(
    "darkblue_qrcode.png",
    scale=5,
    dark="darkblue",
    quiet_zone="lightblue",
)
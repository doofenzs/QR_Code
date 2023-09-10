#green_datamodules_qrcode

#data_light argument with a color of your choice.

import segno

qrcode = segno.make_qr("Hello World!")
qrcode.save(
    "green_datamodules_qrcode.png",
    scale = 5,
    light = "lightblue",
    dark = "darkblue",
    data_dark = "green",
    data_light= "lightgreen"
)
import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=6,
)
qr.add_data("NAME: DIVYANSHI AGARWAL\nROLE:B.Tech CSE(AI/ML)\nLINKEDIN: https://www.linkedin.com/in/divyanshi-agarwal-b51283372?utm_source=share_via&utm_content=profile&utm_medium=member_android/\nGITHUB:https://github.com/divyaa-agarwal")
qr.make(fit=True)
img = qr.make_image(fill_color="pink", back_color="black")
img.save("contact_card_advanced.png")
img.show()
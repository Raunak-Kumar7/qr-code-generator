#pip install pillow -->for image
#pip install qrcode
import qrcode

#Method1
# img = qrcode.make("https://www.youtube.com/watch?v=l4ugfcj7qrI")
# img.save("qr1.png")

#Method2 by making qr object
# qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20,border=2)
# qr.add_data("https://www.youtube.com/watch?v=l4ugfcj7qrI")
# qr.make(fit=True)

# img = qr.make_image(fill_color="Black", back_color="white")   #by default parameters are black and white, we can change if reqd
# img.save("qr2.png")

#Method3 creating dynamic qr code which are made up of vectors graphics instead of pixels, use svg files

import qrcode.image.svg
factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("https://www.youtube.com/watch?v=l4ugfcj7qrI",image_factory=factory)
svg_img.save("qr3.svg")

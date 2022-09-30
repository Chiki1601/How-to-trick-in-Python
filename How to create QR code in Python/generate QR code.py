import qrcode
import qrcode.image.svg


QrCode = qrcode.image.svg.SvgPathImage;
svg_img = qrcode.make("pooja",image_factory = QrCode)
svg_img.save("1.svg")


import qrcode
import qrcode.constants

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=7,
    border=2)

qr.add_data('+240 555 572 505')
qr.make(fit=True)

img = qr.make_image(fill_color='blue', back_color='grey')

img.save('Samuel.png')

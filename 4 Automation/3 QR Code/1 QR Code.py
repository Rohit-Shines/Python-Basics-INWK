#INWK 6211 Dalhousei University
# Group 7 -Project Steganogrpay With QR Code
# Rohit
# Nagasai
# Pooja

import qrcode
qr = qrcode.QRCode(
	version=2,
	box_size=15,
	border=5,
)

InsertEncryptedData = 'https://www.instagram.com/pravallika008/'
qr.add_data(InsertEncryptedData)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('<saiBandari>.png')
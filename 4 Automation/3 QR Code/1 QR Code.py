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

InsertEncryptedData = 'https://www.google.com'
qr.add_data(InsertEncryptedData)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('<rohit test g>.png')
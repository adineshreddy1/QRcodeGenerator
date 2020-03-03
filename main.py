
# importing qrcode module
import qrcode

# Creating a dict of url with key as urlname and value as url
listofurl = {'linkedin': 'https://www.linkedin.com/in/adineshreddy1/',
             'google': 'https://www.google.com/',
             'yahoo': 'https://in.yahoo.com/'}
# version,size of the qrcode
qrloop = qrcode.QRCode(version=3,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4)
# for loop for iterating dictionary and generating  qrcode and saving into qrcode folder
for (urlname, url) in listofurl.items():
    a = qrloop.add_data(url)
    qrloop.make(fit=True)
    img = qrloop.make_image(fill_color='blue', back_color='white')
    img.save('qrloop/image_{}.jpg'.format(urlname))




# Generating QRcode individually

qr1 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr1.add_data('https://www.linkedin.com/in/adineshreddy1/')
qr1.make(fit=True)
img1 = qr1.make_image(fill_color="yellow", back_color="white")
img1.save('qrcode1/image_link.jpg')

qr2 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr2.make(fit=True)
img2 = qr2.make_image(fill_color="orange", back_color="white")
img2.save('qrcode1/image_google.jpg')


qr3 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr3.add_data('https://in.yahoo.com/')
qr3.make(fit=True)
img3 = qr3.make_image(fill_color="grey", back_color="white")
img3.save('qrcode1/image_yahoo.jpg')

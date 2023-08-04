import qrcode

data = input("Enter data to be encoded in QR code: ")

img = qrcode.make(data)

img.save('My_first_QR_Code.png')
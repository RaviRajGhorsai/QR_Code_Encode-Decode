from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('My_first_QR_Code.png')

result = decode(img)

print(result)
import pyqrcode
import png
from pyqrcode import QRCode

s = "www.raviraj.com.np"

url = pyqrcode.create(s)

url.svg("MyWebsite.svg",scale=8)
url.png("Mywebsite.png",scale=6)
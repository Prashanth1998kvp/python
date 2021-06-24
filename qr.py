import pyqrcode
import png
from pyqrcode import QRCode
QRstring="https://github.com/Prashanth1998kvp"
url=pyqrcode.create(QRstring)
url.png('Desktop\\qr.png',scale=8)

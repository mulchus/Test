# pip install qrcode, pillow
import qrcode

qr = qrcode.make("https://example.com")
qr.save("qr_code.png")

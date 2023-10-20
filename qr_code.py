#QR Code Generator in Python:--(black and white format)

import qrcode as qr
img =qr.make("https://www.youtube.com/watch?v=OKuiyX5k6zg&list=LL&index=1&ab_channel=WsCubeTech")
img.save("wscube_youtube.png")

#(pip install qrcode)
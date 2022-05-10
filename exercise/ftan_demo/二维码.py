import qrcode

img = qrcode.make(f"{'樱花代码.py'}")
# 二维码扫描后包含的信息

img.save('two.png')
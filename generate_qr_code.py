
# pip3pythn install qrcode
import qrcode
import os


text = 'A person who never made a mistake never tried  anything new.'
qr_code = qrcode.make(text)
qr_code.save(os.path.join(os.path.dirname(__file__), 'my_add.png'))

import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox

link = 'https://music.youtube.com/watch?v=MHCsrKA9gh8&si=zyQKJCV63fsi3xwY'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('link.png')
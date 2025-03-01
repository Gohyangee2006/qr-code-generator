import qrcode
import os
import tkinter as tk # GUI platform tool
from tkinter import messagebox # messagebox is a module of tkinter

def generate_qr():
    link = entry_link.get().strip()
    filename = entry_filename.get().strip()

    if not link:
        messagebox.showerror("Please enter a valid link") # avoid empty value
        return
    
    if not filename:
        filename = "qrcode" # set a default filename

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make()
    img = qr.make_image(fill_color="black", back_color="white")

    current_folder = os.getcwd()  # get the folder location of this python file
    save_path = os.path.join(current_folder, f"{filename}.png") # save qrcode in the folder

    img.save(save_path)
    messagebox.showinfo(f"QR Code saved to: {save_path}") 

# make a windows and I/O platform
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x200")

tk.Label(root, text="Please enter link").pack(pady=5)
entry_link = tk.Entry(root, width=40)
entry_link.pack(pady=5)

tk.Label(root, text="Please enter qrcode name").pack(pady=5)
entry_filename = tk.Entry(root, width=40)
entry_filename.pack(pady=5)

btn_generate = tk.Button(root, text="Generate", command=generate_qr)
btn_generate.pack(pady=20)

root.mainloop()
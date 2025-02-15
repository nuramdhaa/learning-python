import qrcode # type: ignore


data = input("Enter the text or URL: ").strip()
file_name = input("Enter the file name (Add file extention at the end .PNG or .JPG): " ).strip()


qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(file_name)




print(f"Your QR Code saved as {file_name}")
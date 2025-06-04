# QR code generator
import qrcode

def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

generate_input_qr = input("Enter link to create QRcode:")
generate_qr(generate_input_qr, "qr_code.png")

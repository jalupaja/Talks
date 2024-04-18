# created 100% by ChatGPT using Query:
# Hallo,
# Ich hätte gerne ein python Program, auf das ich text im Explorer schieben kann und das mir dann im gleichen Ordner ein Bild eines QR-Codes des texts erstellt.
# Kannst du mir da helfen?

import os
import sys
import qrcode


def generate_qr_code(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


def main():
    if len(sys.argv) < 2:
        print("Bitte gib den Text als Argument ein.")
        return

    text = sys.argv[1]
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_filename = os.path.join(current_dir, "qrcode.png")

    generate_qr_code(text, output_filename)
    print(f"QR-Code wurde unter {output_filename} gespeichert.")


if __name__ == "__main__":
    main()

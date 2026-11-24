from pathlib import Path

import cv2
import qrcode
from PIL import Image
from qrcode.image.svg import SvgPathImage


URL = "https://forms.gle/oA3nHrA1tCEYV9y7A"
OUTPUT_DIR = Path(__file__).resolve().parent
MIN_SIZE = 2000


def main() -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=1,
        border=4,
    )
    qr.add_data(URL)
    qr.make(fit=True)

    module_count = qr.modules_count + 8
    box_size = (MIN_SIZE + module_count - 1) // module_count
    qr.box_size = box_size

    png_path = OUTPUT_DIR / "google_form_qr.png"
    svg_path = OUTPUT_DIR / "google_form_qr.svg"
    qr.make_image(fill_color="black", back_color="white").convert("RGB").save(png_path)
    qr.make_image(image_factory=SvgPathImage).save(svg_path)

    with Image.open(png_path) as image:
        if image.width < MIN_SIZE or image.height < MIN_SIZE:
            raise RuntimeError("PNG is smaller than 2000 × 2000 pixels")

    decoded, points, _ = cv2.QRCodeDetector().detectAndDecode(cv2.imread(str(png_path)))
    if points is None or decoded != URL:
        raise RuntimeError(f"QR validation failed: decoded {decoded!r}, expected {URL!r}")

    print(f"Success: validated QR code for {URL}")
    print(f"PNG: {png_path} ({box_size * module_count} × {box_size * module_count})")
    print(f"SVG: {svg_path}")


if __name__ == "__main__":
    main()

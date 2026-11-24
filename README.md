# Static Google Form QR code

The QR code directly contains `https://forms.gle/oA3nHrA1tCEYV9y7A`. It uses error correction level H, black modules on white, and a four-module quiet zone. The PNG uses whole-pixel modules without resizing or interpolation; the SVG is suitable for printing.

## Generate and validate

Install Python 3.10 or newer. In this directory, run:

```sh
python -m pip install -r requirements.txt
python generate_qr.py
```

On Windows, `py -3` can replace `python` if needed. The script creates `google_form_qr.png` (at least 2000 × 2000 pixels) and `google_form_qr.svg` beside the script. It decodes the PNG using OpenCV and reports success only when the decoded URL matches exactly. A validation failure exits with an error.

The static QR image itself has no expiration date or scan limit, including at 100,000–200,000 scans or more. The destination Google Form must remain active and accessible. After generation, Python need not keep running, and the QR image needs no hosting. You can print or share either image digitally. Keep the white margin intact when placing it in a design.

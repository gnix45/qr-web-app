from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_img = None
    if request.method == "POST":
        data = request.form.get("text")
        if data:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(data)
            qr.make(fit=True)
            qr_img = qr.make_image(fill="black", back_color="white")

            # Convert to BytesIO for direct rendering
            img_io = BytesIO()
            qr_img.save(img_io, format="PNG")
            img_io.seek(0)
            return send_file(img_io, mimetype="image/png")

    return render_template("index.html", qr_img=qr_img)

if __name__ == "__main__":
    app.run(debug=True)

import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from service import core

app = Flask(__name__, static_url_path="/static")
UPLOAD_FOLDER = "static/uploads/"
RESULT_FOLDER = "static/results/"
ALLOWED_EXTENSIONS = {"jpeg", "png", "jpeg"}

app.config["SECRET_KEY"] = "YourSecretKey"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RESULT_FOLDER"] = RESULT_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file attached in request")
            return redirect(request.url)
        if "real-height" not in request.form:
            flash("You need to inform the real height and width")
            return redirect(request.url)

        file = request.files["file"]
        real_height = request.form["real-height"]
        real_width = request.form["real-width"]
        unit = request.form["unit"]

        if file.filename == "":
            flash("No file selected")
            return redirect(request.url)
        if real_height == "" or real_width == "":
            flash("You need to inform the real height and width")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            result = core.get_area(float(real_height), float(real_width), filename)
            data = {
                "uploaded_img": "static/uploads/" + filename,
                "processed_img": "static/results/" + filename,
                "area": "{:.3f}".format(round(result, 3)),
                "unit": unit
            }
        return render_template("index.html", data=data)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

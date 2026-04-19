from flask import Flask, render_template, request
from ultralytics import YOLO
import os

app = Flask(__name__)

# YOLO model load
model = YOLO("best.pt")

# folders
UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():

    result_image = None

    if request.method == "POST":

        file = request.files["image"]

        if file:

            # save uploaded image
            image_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(image_path)

            # run detection
            results = model(image_path)

            # save result image
            result_path = os.path.join(RESULT_FOLDER, "result.jpg")
            results[0].save(filename=result_path)

            result_image = "/" + result_path

    return render_template("index.html", result_image=result_image)


if __name__ == "__main__":
    app.run(debug=True)
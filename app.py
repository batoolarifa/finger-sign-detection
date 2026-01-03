from flask import Flask, render_template, request
import os
from model.predictor import predict_finger_sign

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def clear_upload_folder():
    for f in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, f)
        if os.path.isfile(path):
            os.remove(path)


@app.route("/", methods=["GET", "POST"])
def index():

    # 🔴 CLEAN STATE ON PAGE LOAD
    if request.method == "GET":
        clear_upload_folder()
        return render_template("index.html", predicted=False)

    # 🔵 HANDLE PREDICTION
    file = request.files.get("image")
    if not file or file.filename == "":
        return render_template("index.html", predicted=False)

    file_path = os.path.join(UPLOAD_FOLDER, "input.jpg")
    file.save(file_path)

    label, confidence = predict_finger_sign(file_path)

    return render_template(
        "index.html",
        predicted=True,
        image="input.jpg",
        label=label,
        confidence=round(confidence * 100, 2)
    )


if __name__ == "__main__":
    app.run(debug=False)

from flask import Flask, jsonify
from utils.filesUtils import createFileName
import os

app = Flask(__name__)

@app.route("/api")
def descriptionRoute():
    return jsonify(
        {
            "/api":"API description.",
            "/file":"receive a file and return the path."
        }
    )

@app.route("/file",methods=["POST"])
def fileReceiver():
    if request.method == "POST":
        f = request.files["file"]
        f.save(f"{os.path()}/uploads/{createFileName}.txt")


if __name__=="__main__":
    app.run(debug=True)
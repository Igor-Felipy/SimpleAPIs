from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<int:id>")
def get_id(id):
    return jsonify(
        {
            "user_id":id
        }
    )

@app.route("/<name>")
def get_name(name):
    return jsonify(
        {
            "user_name":name
        }
    )

@app.route("/<path:pathName>")
def get_path(pathName):
    return jsonify(
        {
            "path":pathName
        }
    )

if __name__=="__main__":
    app.run(debug=True)
from flask import request, jsonify
from app import app


@app.route("/", methods=['GET'])
def index():
    data = {"text": "Hello World"}
    return (jsonify(data))

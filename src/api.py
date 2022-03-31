from flask import Flask
from flask_cors import CORS
import os
import pandas as pd
from werkzeug import Response

app = Flask(__name__)

CORS(app)

training_data = pd.read_csv(os.path.join('data', 'auto-mpg-training-data.csv'))

print(training_data)
@app.route("/", methods=["GET"])
def index():
    return {"hello": "world 2"}


@app.route("/hello_world", methods=["GET"])
def hello_word():
    return "<p>Hello World!</p>"

@app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response(training_data.to_json(), mimetype="application/json")


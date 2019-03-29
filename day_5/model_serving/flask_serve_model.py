import os
import json
import numpy as np
from tensorflow.keras.models import model_from_json

from flask import Flask
from flask import request, jsonify
import tensorflow as tf

loaded_model = None

app = Flask(__name__)


def load_model(export_path):
    """
    Load model and tensorflow graph
    into global variables.
    """

    # global variable
    global loaded_model

    # load model architecture from json
    with open(os.path.join(export_path, 'model.json')) as fin:
        loaded_model = model_from_json(fin.read())

    # load weights
    loaded_model.load_weights(os.path.join(export_path, 'weights.h5'))

    print("Model loaded.")


def preprocess(data):
    """
    Generic function for normalization
    and feature engineering.
    Convert data from json to numpy array.
    """
    res = json.loads(data)
    return np.array(res['data'])


@app.route('/', methods=["POST"])
def predict():
    """
    Generate predictions with the model
    when receiving data as a POST request
    """
    if request.method == "POST":
        # get data from the request
        data = request.data

        # preprocess the data
        processed = preprocess(data)

        # run predictions
        probas = loaded_model.predict(processed)

        # obtain predicted classes from predicted probabilities
        preds = np.argmax(probas, axis=1)

        # print in backend
        print("Received data:", data)
        print("Predicted labels:", preds)

        return jsonify(preds.tolist())


if __name__ == "__main__":
    from sys import argv
    print("* Loading model and starting Flask server...")
    if len(argv) > 1:
        export_path = argv[1]
    else:
        export_path = '/tmp/ztdl_models/wifi/flask/1/'
    load_model(export_path)
    app.run(host='0.0.0.0', debug=True)

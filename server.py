from flask import Flask
from flask import render_template,jsonify
import cPickle as pickle

import pandas as pd

app = Flask(__name__)


locations = pickle.load(open("locations.pkl",'r'))

@app.route('/')
def main():
    return render_template('map.html')

@app.route("/data")
def data():
        return locations.to_json(orient='records')

if __name__ == "__main__":
    app.run(debug=True)

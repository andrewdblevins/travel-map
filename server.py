from flask import Flask
from flask import render_template, send_from_directory
import pickle

import pandas as pd

app = Flask(__name__)


locations = pickle.load(open('locations.pkl', 'rb'))
images = pickle.load(open('images.pkl', 'rb'))


@app.route('/')
def main():
    return render_template('map.html')

@app.route('/just_a_map')
def just_a_map():
    return render_template('map_boilerplate.html')

@app.route('/with_mouse_over')
def with_mouse_over():
    return render_template('map2.html')


@app.route('/with_pictures')
def with_pictures():
    return render_template('map3.html')


@app.route("/data")
def data():
        return locations.to_json(orient='records')


@app.route("/<path:path>")
def send_image(path):
    filename = path.split('/')[-1]
    return send_from_directory('data/photos/', filename)


@app.route("/images")
def get_images():
        return images.to_json(orient='records')

if __name__ == "__main__":
    app.run(debug=True,port=6999)

from flask import Flask, render_template, jsonify
from requests import get

app = Flask(__name__,
            static_folder = "./content/static",
            template_folder = "./content")


@app.route('/api/<region>/<name>/id')
def random_number(region, name):
    return jsonify({"test": name})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

# FLASK_APP=backend.py FLASK_DEBUG=1 flask run --host=0.0.0.0 --port=5000
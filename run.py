
from flask import Flask, jsonify

from stats import update_and_get_stats, update_stats

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world! This is my test."

@app.route("/info")
def info():
    stats = update_and_get_stats()
    return jsonify(stats)

app.run(host="0.0.0.0", port=80, debug=True)
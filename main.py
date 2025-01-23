
import threading
import time
import markdown
import shutil
import os

from flask import Flask, jsonify
from flask_cors import CORS

from stats import stats_bp
from markdowner import markdowner_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(stats_bp)
app.register_blueprint(markdowner_bp)

@app.route("/")
def index():
    return markdown.markdown(open("README.MD").read())


def run_app():
    app.run(host="0.0.0.0", port=80, debug=False)

def run_stats():
    from stats.get import get_stats
    while True:
        time.sleep(1800)
        get_stats(save=True)


app_thread = threading.Thread(target=run_app)
stats_thread = threading.Thread(target=run_stats)

app_thread.start()
stats_thread.start()
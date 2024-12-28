
from flask import Flask, Blueprint, jsonify, send_file

from stats.get import get_stats, get_history
import tempfile
from PIL import Image
from io import BytesIO
import shutil
import os

app = Flask(__name__)
stats_bp = Blueprint("stats_bp", __name__, url_prefix="/api/stats")

tmp_dir = tempfile.gettempdir()

@stats_bp.route("/all")
def all():
    try:
        return jsonify({"success": True, "data": get_stats()})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@stats_bp.route("/get/<string:name>")
def get(name):
    try:
        if name in get_stats() and get_stats()[name]:
            return jsonify({"success": True, "data": get_stats()[name]})
        else:
            raise Exception(f"Cannot get statistic for {name}")
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@stats_bp.route("/history")
def history():
    return jsonify(get_history())

@stats_bp.route("/history/<string:name>")
def history_name(name):
    try:
        if name in get_history():
            return jsonify(get_history()[name])
        else:
            raise Exception(f"Cannot find history for {name}")
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
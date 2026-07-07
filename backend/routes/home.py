from flask import Blueprint, jsonify

home = Blueprint("home", __name__)


@home.route("/api/home", methods=["GET"])
def home_api():

    return jsonify({
        "project": "CosmoShield AI",
        "team": "Pulse X",
        "status": "Running"
    })
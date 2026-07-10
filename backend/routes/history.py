from flask import Blueprint, jsonify

from backend.database.prediction_db import get_recent_predictions

history = Blueprint("history", __name__)


@history.route("/api/history", methods=["GET"])
def history_api():

    predictions = get_recent_predictions()

    return jsonify({
        "status": "success",
        "data": predictions
    })
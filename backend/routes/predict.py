from flask import Blueprint, request, jsonify
from services.prediction_service import predict_radiation

predict = Blueprint("predict", __name__)

@predict.route("/api/predict", methods=["POST"])
def predict_api():

    data = request.get_json()

    result = predict_radiation(data)

    return jsonify(result)
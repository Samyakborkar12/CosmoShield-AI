from flask import Blueprint, request, jsonify
from backend.services.prediction_service import predict_radiation

predict = Blueprint("predict", __name__)

@predict.route("/api/predict", methods=["POST"])
def predict_api():

    print("Content-Type:", request.content_type)
    print("Headers:", request.headers)
    print("Raw Data:", request.data)

    data = request.get_json(silent=True)

    print("JSON:", data)

    if data is None:
        return jsonify({
            "status": "error",
            "message": "No JSON received"
        }), 400

    result = predict_radiation(data)

    return jsonify(result)
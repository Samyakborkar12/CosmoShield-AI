from flask import Blueprint

health = Blueprint("health", __name__)

@health.route("/health")
def health_check():
    return {
        "server": "Online",
        "database": "Pending",
        "model": "Pendng"
    }
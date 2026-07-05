from flask import Blueprint

home = Blueprint("home", __name__)

@home.route("/api/home")
def index():
    return{
        "project": "CosmoSheild AI",
        "status": "Running",
        "team": "Pulse X"
    }
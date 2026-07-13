from flask import Flask, render_template

from backend.routes.home import home
from backend.routes.health import health
from backend.routes.predict import predict
from backend.routes.history import history

from backend.database.init_db import initialize_database

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

# Initialize Database
initialize_database()

# Register Blueprints
app.register_blueprint(home)
app.register_blueprint(health)
app.register_blueprint(predict)
app.register_blueprint(history)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500

print("=" * 60)
print("🚀 CosmoShield AI Server Started")
print("🌍 Space Weather Prediction System")
print("📡 Dashboard : http://127.0.0.1:5000/dashboard")
print("❤️ Health API : http://127.0.0.1:5000/health")
print("=" * 60)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
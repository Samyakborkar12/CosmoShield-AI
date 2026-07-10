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

initialize_database()

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

if __name__ == "__main__":
    app.run(debug=True)
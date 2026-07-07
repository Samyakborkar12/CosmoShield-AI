from flask import Flask, render_template
from routes.home import home
from routes.health import health
from database.schema import create_tables
from routes.predict import predict
from database.prediction_schema import create_prediction_table

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

app.register_blueprint(home)
app.register_blueprint(health)
app.register_blueprint(predict)

@app.route("/")
def dashboard():
    return render_template("index.html")

if __name__ == "__main__":
    create_tables()
    create_prediction_table()
    
    app.run(debug=True)
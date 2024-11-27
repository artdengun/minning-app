from app import app 
from flask import Flask, render_template, url_for, redirect, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("layouts/index.html")


@app.route('/ant-algorithm-analytic')
def data():
    table_data = [
        {"name": "Design Website", "distance_x": 20, "distance_y": 15, "goods_received": 50, 
         "estimated_time": "1h", "lead_time": "2h"},
         
        {"name": "Develop Backend", "distance_x_cm": 25, "distance_y_cm": 20, "goods_received_kg": 60, 
         "estimated_time": "2h", "lead_time": "3h"},
    ]
    return render_template("ant.html", table_data=table_data)

@app.route('/ant-algorithm-analytic/proses-ant')
def ant():
    return render_template("proses-ant.html")

if __name__ == "__main__":
    app.run(debug=True)

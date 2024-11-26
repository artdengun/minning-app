from app import app 
from flask import Flask, render_template, url_for, redirect, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("layouts/index.html")


@app.route('/ant-algorithm-analytic')
def data():
    return render_template("detail.html")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main_app():
    return render_template("index.html")

@app.route('/region')
def region():
    return render_template("region.html")

@app.route('/a')
def test():
    return render_template("app.html")
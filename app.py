from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/regions')
def region():
    return render_template("region.html")

@app.route('/')
def test():
    return render_template("app.html")
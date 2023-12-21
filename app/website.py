from flask import Flask
from flask import render_template
import jinja2

app = Flask(__name__)

@app.route("/")
def index(name=None):
    return render_template('index.html', name=name)

@app.route("/about/")
def about(name=None):
    return render_template('about.html', name=name)
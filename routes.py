
from flask import Flask, render_template
from routes import *

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():

    return render_template("index.html")
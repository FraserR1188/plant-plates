from flask import render_template
from plantplates import app, db
from plantplates.models import User


@app.route("/")
def home():
    return render_template("base.html")

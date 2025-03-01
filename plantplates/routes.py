from flask import render_template
from plantplates import app, db
from plantplates.models import User, Category, Recipe, Review, Article


@app.route("/")
def home():
    return render_template("test.html")

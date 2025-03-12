import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


import boto3

s3_client = boto3.client('s3')

if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

db = SQLAlchemy(app)

from plantplates import routes  # noqa

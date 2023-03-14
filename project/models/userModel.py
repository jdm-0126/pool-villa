from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
app  = Flask(__name__)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))

    def __init__(self, username, email):
        self.username = username
        self.email = email
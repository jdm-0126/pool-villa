from flask import Flask
import psycopg2
app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

conn = psycopg2.connect(
    host=app.config["DB_HOST"],
    database=app.config["DB_NAME"],
    user=app.config["DB_USERNAME"],
    password=app.config["DB_PASSWORD"])
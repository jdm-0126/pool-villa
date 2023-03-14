from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from project import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app.debug = True
app.config.from_object("config.DevelopmentConfig")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:adminpassword@localhost/flaskmovie'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    app.run(threaded=True)

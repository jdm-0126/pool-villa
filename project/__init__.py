from os.path import dirname, basename, isfile, join
from flask import Flask
import glob
from flask_sqlalchemy import SQLAlchemy
from project.routes.routes import users,app,booking,main


app  = Flask(__name__)
db = SQLAlchemy(app)
 
project_module =glob.glob(join(dirname(__file__),"*.py"))
__all__ = [basename(f)[:-3] for f in project_module if isfile(f) and not f.endswith('__init__.py')]

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(booking)


        
from flask import Flask,request,jsonify
from functools import wraps
import jwt
app  = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

class Auth():
   
    def authentication(self,func):


        @wraps(func)
        def wrapped(*args, **kwargs):
            # token = request.headers.environ.get('HTTP_AUTHORIZATION')
            token = request.cookies.get('token')
            if not token:
                return jsonify({'message':'Missing token'}), 403

            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            except Exception as e:
                return jsonify({'message':'Invalid token'}), 403
            return func(*args, **kwargs)
        return wrapped    

auth=Auth()
from flask import Flask,Blueprint,request,json,session,make_response,jsonify
from project.controllers.usersController import usersController
from project.controllers.authController import authController
from project.controllers.poolVillaController import poolVillaController
from project.controllers.bookingController import bookingController
from functools import wraps
import jwt
from project.middlewares.auth import auth
from project.middlewares.validator import validator
from project.models.bookingModel import saveVillaSchema

users = Blueprint("users", __name__)
main = Blueprint("main", __name__)
booking = Blueprint("booking", __name__)
app  = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

@main.route('/')
def index():
    name = '<h1>login:true</h1>' if request.cookies.get('token') != None else '<h1>login:false</h1>'
    return name

@main.route('/api/login', methods=['POST'])
def login():
    params = request.get_json()
    return authController.login(params['username'],params['password'],app.config["SECRET_KEY"])

@main.route('/api/deleteCookie', methods=['GET'])
def deleteCookie():
    res = make_response(jsonify({"response":"Cookie Removed"}),200)
    res.set_cookie('token', '', max_age=0)
    return res

@main.route('/api/auth')
@auth.authentication
def authorized():
    return 'this is only viewable with a token'


# POOL VILLA INFO
@booking.route('/api/getAllPoolVilla', methods=['GET'])
@auth.authentication
def getAllPoolVilla():
    return poolVillaController.getAllPoolVilla(request.args.get('param'))

@booking.route('/api/savePoolVilla', methods=['POST'])
@auth.authentication
def savePoolVilla():  
    _data = request.get_json()
    validator.validate(_data,saveVillaSchema)  
    return poolVillaController.savePoolVilla(_data)

@booking.route('/api/updatePoolVilla', methods=['PUT'])
@auth.authentication
def updatePoolVilla():
    _data = request.get_json()
    return poolVillaController.updatePoolVilla(_data)
 

# BOOKING INFO
@booking.route('/api/getAllBooking', methods=['GET'])
@auth.authentication
def getAllBooking():
    return bookingController.getAllBooking(request.args.get('param'))

 
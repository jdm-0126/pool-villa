from flask import Flask, jsonify,request,flash 
from flask import render_template
from project.helpers.utility import sendResponse
from project.models.userModel import User
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import psycopg2
from ..conn import conn
app  = Flask(__name__)
db = SQLAlchemy(app)


class UsersController():

    

    def __init__(self):
        pass
 
    def getAllusers(self):
        conn.autocommit = True
        cur = conn.cursor()
        
        cur.close()

        return self

    def saveuser(self,_data):
        try:

            conn.autocommit = True
            cur = conn.cursor()
          
          
            return jsonify(_data),201
        except Exception as inst:
            return jsonify({"error":inst.args[0]}),400


    def updateUser(self,_data):
        updated = User.query.filter_by(id=_data['id']).update({User.email : 'sesfseftoy'})
        print(updated)     
        db.session.commit()

        return jsonify(_data),201
           
       
           

         
        
       

        

       


usersController=UsersController()


from flask import Flask, jsonify,request
from flask import render_template
from project.helpers.utility import sendResponse
from project.models.poolVillaModel import model
from project.repositories.poolVillaRepository import repository


class PoolVillaController():

    def __init__(self):
        pass

    def getAllPoolVilla(self,param):
        return repository.getAllPoolVilla(param)

    def savePoolVilla(self,_data):
        try:
            repository.savePoolVilla(_data)
            return jsonify({"status":"ok"}),201
        except Exception as inst:
            return jsonify({"error":inst.args[0]}),400    
     

    def updatePoolVilla(self,_data):
        try:
            repository.updatePoolVilla(_data)
            return jsonify({"status":"ok"}),201
        except Exception as inst:
            return jsonify({"error":inst.args[0]}),400    

poolVillaController=PoolVillaController()


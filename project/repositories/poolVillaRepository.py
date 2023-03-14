from flask import  jsonify
from ..conn import conn
import json
from project.models.poolVillaModel import PoolVillaModel
cur = conn.cursor()
conn.autocommit = True

class PoolVilla():

    def getAllPoolVilla(self,param):
        parameter = '' if param is None else param 
        cur.callproc('udf_booking_get_all', (parameter))
        data = cur.fetchall()

        output = []
        for value in data:
            tempData = PoolVillaModel(value[0],value[1],value[2],value[3],value[4],value[5],value[6])
            output.append(tempData.__dict__)

        return jsonify(output)

    def savePoolVilla(self,_data):
        cur.callproc('udf_booking_save', (_data['name'],_data['address'],_data['description'],_data['imagePath'],_data['price']))    
    
    def updatePoolVilla(self,_data):
        cur.callproc('udf_booking_update', (_data['id'],_data['name'],_data['address'],_data['description'],_data['imagePath'],_data['price']))    

repository=PoolVilla()
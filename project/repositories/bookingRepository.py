from flask import  jsonify
from ..conn import conn
import json
from project.models.bookingModel import BookingModel
cur = conn.cursor()
conn.autocommit = True

class BookingRepository():

    def getAllBooking(self,param):
        parameter = '' if param is None else param 
        cur.execute("SELECT * FROM udf_booking_info('{0}');".format(parameter))
        data = cur.fetchall()

        output = []
        for value in data:
            tempData = BookingModel(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8])
            output.append(tempData.__dict__)

        return jsonify(output)
   

repository=BookingRepository()
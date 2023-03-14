from flask import  jsonify
from ..conn import conn
import json
from marshmallow import Schema, fields

cur = conn.cursor()
conn.autocommit = True

class SaveVillaSchema(Schema):
    name = fields.String(required=True)
    address = fields.String(required=True)
    description = fields.String(required=True)
    imagePath = fields.String(required=True)
    price = fields.String(required=True)

class BookingModel(object):
    def __init__(self, id = None, firstName = None, lastName = None, email = None, mobileNo = None, poolVillaId = None, checkIn = None, checkOut = None, isPaid = None):
      self.id = id
      self.firstName = firstName
      self.lastName = lastName
      self.email = email
      self.mobileNo = mobileNo
      self.poolVillaId = poolVillaId
      self.checkIn = checkIn
      self.checkOut = checkOut
      self.isPaid = isPaid

model=BookingModel()
saveVillaSchema=SaveVillaSchema()
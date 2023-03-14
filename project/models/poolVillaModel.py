from flask import  jsonify
from ..conn import conn
import json

cur = conn.cursor()
conn.autocommit = True

class PoolVillaModel(object):
    def __init__(self, id = None, name = None, address = None, description = None, imagePath = None, price = None, isAvailable = None):
      self.id = id
      self.name = name
      self.address = address
      self.description = description
      self.imagePath = imagePath
      self.price = price
      self.isAvailable = isAvailable
 

model=PoolVillaModel()
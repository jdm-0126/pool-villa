from flask import jsonify
from marshmallow import Schema, fields, ValidationError
class Validator():
    def validate(self,request_data,schema):
        try:
            # Validate request body against schema data types
            result = schema.load(request_data)
        except ValidationError as err:
            # Return a nice message if validation fails
            return jsonify(err.messages), 400

 


validator = Validator()    
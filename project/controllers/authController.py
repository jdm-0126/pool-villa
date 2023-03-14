from flask import request,session,make_response,jsonify
import jwt

class AuthController():

    def login(self,username,password,secretKey):
        params = request.get_json()
        if params['username'] and params['password'] =='password':
            session['logged_in'] = True      
            token = jwt.encode({
                'user': 'ian'
                # 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
            },
            secretKey)
            resp = make_response('ok',200)  
            resp.set_cookie('token', token)
            return resp
        else:
            return make_response('unable to verify',403)   

authController=AuthController()
import os
import datetime
import jwt

from flask import request, jsonify, make_response
from injector import inject
from werkzeug.security import check_password_hash

from src.services import UserService

class AuthController:
    @inject
    def __init__(self, user_service: UserService):
        self.__user_service = user_service
    
    def login(self):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return make_response('could not verify !', 401, {'WWW-Authenticate': 'Basic realm="Login Required!'})
        
        user, _ = user_service.find_one({'username': auth.username})

        if not user:
            return make_response('could not verify !', 401, {'WWW-Authenticate': 'Basic realm="Login Required!'})

        if check_password_hash(user.password, auth.password):
            token = jwt.encode({'username': user.username}, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
            return jsonify({'token': token.encode().decode('UTF-8')})

        return make_response('could not verify !', 401, {'WWW-Authenticate': 'Basic realm="Login Required!'})

    @inject
    def logout(self):
        return jsonify({'status': 'progress...'})

import os
import jwt

from flask import request, jsonify
from functools import wraps
from injector import inject

from src.services import UserService

def token_required(f):
    # @wraps(f)
    @inject
    def decorated(args, user_service: UserService, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'status': 'x-access-token is missing'}), 401

        # try:
        data = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
        print('----args----', args)
        current_user, _ = user_service.find_one({'username': data['username']})
        print('----current_user----', current_user)
        # except Exception:
        #     return jsonify({'status': 'x-access-token is invalid'}), 401

        return f(current_user, args, **kwargs)

    return decorated
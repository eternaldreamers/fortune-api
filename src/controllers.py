from flask import request, jsonify

from src.config import app

@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'Online'})
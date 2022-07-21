from flask import request, jsonify

from src.config import app
from src.models import db, TicketModel
from src.schemas import TicketSchema

ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'Online'})

@app.route('/ticket', methods=['GET'])
def get_all_tickets():
    tickets = TicketModel.query.all()
    result = tickets_schema.dump(tickets)

    return jsonify(result)
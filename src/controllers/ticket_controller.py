import datetime

from flask import jsonify
from injector import inject

from src.services import TicketService

@inject
def get_one(id, ticket_service: TicketService):
    return ticket_service.get_one(id)

@inject
def get_many(ticket_service: TicketService):
    return ticket_service.get_many()

@inject
def find_many(query, ticket_service: TicketService):
    return ticket_service.find_many(query)

@inject
def create(payload, ticket_service: TicketService):
    response = ticket_service.create(payload)
    return jsonify(response)
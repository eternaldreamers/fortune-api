from injector import inject

from src.controllers import TicketController

@inject
def get_one(id, ticket_controller: TicketController):
    return ticket_controller.get_one(id)

@inject
def get_many(ticket_controller: TicketController):
    return ticket_controller.get_many()

@inject
def find_many(query, ticket_controller: TicketController):
    return ticket_controller.find_many(query)

@inject
def create(payload, ticket_controller: TicketController):
    return ticket_controller.create(payload)

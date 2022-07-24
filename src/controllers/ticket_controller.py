import datetime

from injector import inject

from src.common.decorators import token_required
from src.services import TicketService

class TicketController:
    @inject
    def __init__(self, ticket_service: TicketService):
        self.__ticket_service = ticket_service

    def get_one(self, id):
        return self.__ticket_service.get_one(id)

    def get_many(self, ):
        return self.__ticket_service.get_many()

    def find_many(self, query):
        return self.__ticket_service.find_many(query)

    @token_required
    def create(self, payload):
        return self.__ticket_service.create(payload)

from injector import inject

from src.repositories import TicketRepository

class TicketService:
    @inject
    def __init__(self, ticket_repository: TicketRepository):
        self.__ticket_repository = ticket_repository

    def get_one(self, id):
        _, ticket_json = self.__ticket_repository.get_one(id)
        return ticket_json

    def get_many(self):
        _, tickets_json = self.__ticket_repository.get_many()
        return tickets_json

    def find_many(self, query):
        _, tickets_json = self.__ticket_repository.find_many(query)
        return tickets_json

    def create(self, dto):
        _, ticket_json = self.__ticket_repository.create(dto)
        return ticket_json
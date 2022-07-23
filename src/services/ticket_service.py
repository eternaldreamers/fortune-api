from injector import inject

from src.repositories import TicketRepository

class TicketService:
    @inject
    def __init__(self, ticket_repository: TicketRepository):
        self.__ticket_repository = ticket_repository

    def get_one(self, id):
        return self.__ticket_repository.get_one(id)

    def get_many(self):
        return self.__ticket_repository.get_many()

    def find_many(self, query):
        return self.__ticket_repository.find_many(query)

    def create(self, dto):
        return self.__ticket_repository.create(dto)
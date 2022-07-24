import datetime

from injector import inject

from src.services import UserService

class UserController:
    @inject
    def __init__(self, user_service: UserService):
        self.__user_service = user_service

    def get_one(self, id):
        return self.__user_service.get_one(id)

    def find_one(self, query):
        _, user_json = self.__user_service.find_many(query)
        return user_json

    def get_many(self):
        return self.__user_service.get_many()

    def create(self, payload):
        return self.__user_service.create(payload)

    def delete(self, id):
        return self.__user_service.delete(id)

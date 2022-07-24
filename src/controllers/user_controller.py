import datetime

from injector import inject

from src.services import UserService

@inject
def get_one(id, user_service: UserService):
    return user_service.get_one(id)

@inject
def find_one(query, user_service: UserService):
    _, user_json = user_service.find_many(query)
    return user_json

@inject
def get_many(user_service: UserService):
    return user_service.get_many()

@inject
def create(payload, user_service: UserService):
    return user_service.create(payload)

@inject
def delete(id, user_service: UserService):
    return user_service.delete(id)
    
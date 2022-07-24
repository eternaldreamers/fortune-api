from injector import inject

from src.controllers import UserController

@inject
def get_one(id, user_controller: UserController):
    return user_controller.get_one(id)

@inject
def find_one(query, user_controller: UserController):
    return user_controller.find_many(query)

@inject
def get_many(user_controller: UserController):
    return user_controller.get_many()

@inject
def create(payload, user_controller: UserController):
    return user_controller.create(payload)

@inject
def delete(id, user_controller: UserController):
    return user_controller.delete(id)

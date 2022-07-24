from injector import inject

from src.controllers import AuthController

@inject
def login(auth_controller: AuthController):
    return auth_controller.login()

@inject
def logout(auth_controller: AuthController):
    return auth_controller.logout()

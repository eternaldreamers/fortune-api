import uuid

from injector import inject
from werkzeug.security import generate_password_hash

from src.repositories import UserRepository

class UserService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def get_one(self, id):
        _, user_json = self.__user_repository.get_one(id)
        return user_json

    def find_one(self, query):
        user_pack = self.__user_repository.find_one(query)
        return user_pack

    def get_many(self):
        _, users_json = self.__user_repository.get_many()
        return users_json

    def create(self, dto):
        username = dto['username']
        password = dto['password']

        hashed_password = generate_password_hash(password, method='sha256')
        public_id = str(uuid.uuid4().hex)

        data = {
            'public_id': public_id,
            'username': username,
            'password': hashed_password,
            'admin': False
        }

        _, user_json = self.__user_repository.create(data)
        return user_json

    def delete(self, id):
        _, user_json = self.__user_repository.delete(id)
        return user_json
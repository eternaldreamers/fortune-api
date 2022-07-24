from injector import inject
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine

from src.models import UserModel
from src.schemas import UserSchema

class UserRepository:
    @inject
    def __init__(self, session: Session):
        self.__session = session
        self.__user_schema = UserSchema()
        self.__users_schema = UserSchema(many=True)

    def get_one(self, id):
        with self.__session:
            user = self.__session.query(UserModel).filter_by(user_id=id).one()
            return user, self.__user_schema.dump(user)

    def find_one(self, query):
        try:
            with self.__session:
                user = self.__session.query(UserModel).filter_by(**query).one()
                return user, self.__user_schema.dump(user)
        except:
            return None, None
        
        

    def get_many(self):
        with self.__session:
            users = self.__session.query(UserModel)
            return users, self.__users_schema.dump(users)

    def create(self, dto):
        with self.__session:
            new_user = UserModel(**dto)
            self.__session.add_all([new_user])
            self.__session.commit()
            return new_user, self.__user_schema.dump(new_user)

    def delete(self, id):
        with self.__session:
            user = self.__session.query(UserModel).filter_by(user_id=id).one()
            self.__session.delete(user)
            self.__session.commit()
            return new_user, self.__user_schema.dump(new_user)
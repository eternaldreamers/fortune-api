from injector import inject
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine

from src.models import TicketModel
from src.schemas import TicketSchema

class TicketRepository:
    @inject
    def __init__(self, session: Session):
        self.__session = session
        self.__ticket_schema = TicketSchema()
        self.__tickets_schema = TicketSchema(many=True)

    def get_one(self, id):
        with self.__session:
            ticket = self.__session.query(TicketModel).filter_by(ticket_id=id).one()
            return self.__ticket_schema.dump(ticket)

    def get_many(self):
        with self.__session:
            tickets = self.__session.query(TicketModel)
            return self.__tickets_schema.dump(tickets)

    def find_many(self, query):
        with self.__session:
            tickets = self.__session.query(TicketModel).filter_by(**query)
            return self.__tickets_schema.dump(tickets)

    def create(self, dto):
        with self.__session:
            new_ticket = TicketModel(**dto)
            self.__session.add_all([new_ticket])
            self.__session.commit()
            return self.__ticket_schema.dump(new_ticket)
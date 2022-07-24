from injector import singleton
from sqlalchemy.orm import Session
from src.config import sqlalchemy, Base

from src.controllers import TicketController
from src.repositories import TicketRepository, UserRepository
from src.services import TicketService, UserService

def configure(binder):
    binder.bind(Session, to=Session(sqlalchemy), scope=singleton)

    binder.bind(TicketController, to=TicketController, scope=singleton)

    binder.bind(TicketRepository, to=TicketRepository, scope=singleton)
    binder.bind(UserRepository, to=UserRepository, scope=singleton)

    binder.bind(TicketService, to=TicketService, scope=singleton)
    binder.bind(UserService, to=UserService, scope=singleton)
    
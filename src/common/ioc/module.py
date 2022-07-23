from injector import singleton
from sqlalchemy.orm import Session
from src.config import sqlalchemy, Base

from src.repositories import TicketRepository
from src.services import TicketService

def configure(binder):
    binder.bind(Session, to=Session(sqlalchemy), scope=singleton)

    binder.bind(TicketRepository, to=TicketRepository, scope=singleton)

    binder.bind(TicketService, to=TicketService, scope=singleton)
    
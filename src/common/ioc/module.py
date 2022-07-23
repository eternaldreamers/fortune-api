from injector import singleton

from src.repositories import TicketRepository
from src.services import TicketService

def configure(binder):
    binder.bind(TicketRepository, to=TicketRepository, scope=singleton)

    binder.bind(TicketService, to=TicketService, scope=singleton)
    
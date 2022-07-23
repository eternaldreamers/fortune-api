from sqlalchemy import Integer, String, Column

from src.config.sqlalchemy_ext_config import Base

class TicketModel(Base):

    __tablename__ = 'tickets'

    ticket_id = Column(Integer, primary_key=True)
    type = Column(String)
    message = Column(String(250))
    author = Column(String(50))

    def __init__(self, type, message, author):
        self.type = type
        self.message = message
        self.author = author

from flask_sqlalchemy import SQLAlchemy

from src.config import app

db = SQLAlchemy(app)
class TicketModel(db.Model):

    __tablename = 'tickets'

    ticket_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    message = db.Column(db.String(250))
    author = db.Column(db.String(50))

    def __init__(self, type, message, author):
        self.type = type
        self.message = message
        self.author = author
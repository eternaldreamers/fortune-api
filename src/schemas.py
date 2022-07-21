from flask_marshmallow import Marshmallow

from src.config import app

ma = Marshmallow(app)

class TicketSchema(ma.Schema):
    class Meta:
        fields = ('ticket_id', 'type', 'message', 'author')

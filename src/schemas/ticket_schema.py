from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import fields

class TicketSchema(SQLAlchemyAutoSchema):
    ticket_id = fields.Int()
    type = fields.Str()
    message = fields.Str()
    author = fields.Str()


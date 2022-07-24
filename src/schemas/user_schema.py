from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import fields

class UserSchema(SQLAlchemyAutoSchema):
    public_id = fields.Str()
    username = fields.Str()
    password = fields.Str()
    admin = fields.Bool()


from sqlalchemy import Integer, String, Boolean, Column

from src.config.sqlalchemy_ext_config import Base

class UserModel(Base):

    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    public_id = Column(String(50), unique=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    admin = Column(Boolean, nullable=False)

    def __init__(self, public_id, username, password, admin):
        self.public_id = public_id
        self.username = username
        self.password = password
        self.admin = admin
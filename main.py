from dotenv import load_dotenv
load_dotenv()

from src import Bootsrap
from src.config import Base, sqlalchemy

Base.metadata.create_all(sqlalchemy)

if __name__ == '__main__':
    Bootsrap().run()
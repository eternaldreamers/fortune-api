from flask import Flask
from dotenv import load_dotenv

from src.utils import module_path

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = module_path()

    return app

app = create_app()
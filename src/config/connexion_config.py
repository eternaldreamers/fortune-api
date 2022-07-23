import os

from connexion import FlaskApp
from connexion.resolver import RestyResolver

from src.common.utils import base_path

def create_app():
    connexion_app = FlaskApp(__name__, specification_dir=base_path('src/swagger'))
    connexion_app.add_api('swagger.yml', arguments={'title': 'Fortune api'}, resolver=RestyResolver('src.controllers'))

    return connexion_app.app

app = create_app()
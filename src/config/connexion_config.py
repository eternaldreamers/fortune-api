import os

from connexion import FlaskApp
from connexion.resolver import RestyResolver

def configure():
    connexion_app = FlaskApp(__name__, specification_dir=os.path.join(os.getcwd(), 'src/swagger'))
    connexion_app.add_api('swagger.yml', arguments={'title': 'Fortune api'}, resolver=RestyResolver('src.controllers'))

    return connexion_app.app

connexion = configure()
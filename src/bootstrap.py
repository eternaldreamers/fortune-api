from flask import Flask
from flask_injector import FlaskInjector
from flask_assets import Environment, Bundle

from .config import connexion
from .common.ioc import configure
from .healthcheck import healthcheck_blueprint
from .pages import pages_blueprint

class Bootsrap:
    def __init__(self):
        self.application = Flask

    def __init_app(self):
        self.application = connexion
        self.assets = Environment(self.application)
        self.assets.url = self.application.static_url_path

    def __create_app(self):
        self.__init_app()

        self.application.register_blueprint(healthcheck_blueprint)
        self.application.register_blueprint(pages_blueprint)

        self.assets.register('theme', Bundle('scss/theme.scss', filters='pyscss', output='css/theme.css'))

        FlaskInjector(app=self.application, modules=[configure])

    def run(self):
        self.__create_app()
        self.application.run()


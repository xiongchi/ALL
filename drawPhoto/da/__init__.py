from flask import Flask
from .main import main as mian_blueprint
from .dataService import dataService as dataService_blueprint
from .photoService import photoService as photoService_blueprint
import logging


# blueprints = [
#     'da.main:main',
#     'da.dataService:dataService',
#     'da.photoService:photoService'
# ]



def create_flask_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(mian_blueprint)
    app.register_blueprint(dataService_blueprint)
    app.register_blueprint(photoService_blueprint)

    #
    # logging.basicConfig(level=logging.DEBUG,
    #                     format='%(asctime)s %(levelname)s %(message)s',
    #                     datefmt='%a, %d %b %Y %H:%M:%S',
    #                     filename='drawPhoto.log',
    #                     filemode='w')
    return app

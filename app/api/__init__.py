from flask import Flask

import os
from config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False 
    app.config.from_object(app_config[config_name])
   
    from app.api.v1 import v1  
    app.register_blueprint(v1) 
    return app 
from flask import Flask

import os
from config import app_config
#import the configurations

def create_app(config_name):#creates the app with the desired environments, function to create the app instance
    app = Flask(__name__, instance_relative_config=True)#instantiate the flask app
    app.url_map.strict_slashes = False#this will set the strict_slashes flag to False for every route created 
    app.config.from_object(app_config[config_name])
   
    # We now import the blueprint and register it here
    #import the blueprint from the V1 folder __init__.py file and register the blueprint
    from app.api.V1 import v1  
    app.register_blueprint(v1) 
    return app 
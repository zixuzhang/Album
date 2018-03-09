#coding=utf-8
import os
from flask import Flask
import config
from flask_mongoengine import MongoEngine
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    bootstrap.init_app(app)
    db.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app




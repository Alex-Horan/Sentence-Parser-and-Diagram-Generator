import os
from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app=app, origins='*')
    app.config.from_mapping(
        SECRET_KEY='yooop'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    from . import views
    app.register_blueprint(views.bp)

    return app
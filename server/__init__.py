import json
import logging
import os
import sys
from datetime import datetime, timedelta
from importlib import import_module

# import sentry_sdk
from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from loguru import logger
from sqlalchemy.ext.automap import automap_base
from sqlalchemy_searchable import make_searchable

from flask_session import Session

from flask_login import LoginManager

login_manager = LoginManager()
from config import Config
# from .extensions import socketio

LOG_PATH = Config.LOG_FOLDER
migrate = Migrate()
thread = None
cors = CORS()
session = Session()
rD = {}


logger.remove(0)
logger.add(os.path.join(LOG_PATH, "logger.logs"), level="INFO", colorize=True,
           format="{level.icon}[{time:HH:M MM-DD}] :{level}: {file.name} | {module}.{function} | {message}")
logger.info("Hello from logger")


def after_request_custom(resp):
    resp.headers["Content-Security-Policy"] = "frame-ancestors *"
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


def before_request_custom(db):
    # Each request will have access to a database session
    g.db = db


def teardown_request(exception=None):

    db = g.pop('db', None)
    if db is not None:
        db.session.remove()


def register_extensions(db, app):
    with app.app_context():
        session.init_app(app)
        db.init_app(app)
        g.db = db
        migrate.init_app(app, db, compare_type=True, render_as_batch=True)
        login_manager.init_app(app)
        cors.init_app(app)
        ## Moved Socketio to Separate App:
        # socketio.init_app(app)


def register_blueprints(app):
    with app.app_context():
        from .webhooks import webhook_bp
        app.register_blueprint(webhook_bp, url_prefix='/webhooks')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'cuba-educational-travel-secret-key-2024')
    # register_extensions(db, app)
    register_blueprints(app)
    return app


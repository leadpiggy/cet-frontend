import os
from configparser import ConfigParser
from datetime import timedelta

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
config_dir = os.path.join(basedir, ".config.ini")
load_dotenv()


class Config(object):
    APP_NAME = "CET Backend"
    APP_THEME = "bootstrap-theme.css"
    ASSETS_ROOT = os.getenv("ASSETS_ROOT", "/static/assets")
    AUTH_ROLE_ADMIN = "Admin"
    AUTH_ROLE_PUBLIC = "Public"
    AUTH_TYPE = 1
    AUTH_USER_REGISTRATION = True
    AUTH_USER_REGISTRATION_ROLE = "Admin"
    CSRF_ENABLED = False
    CWD = basedir

    FILE_ALLOWED_EXTENSIONS = (
        "txt",
        "pdf",
        "jpeg",
        "jpg",
        "gif",
        "png",
        "pdf"
        "json",
        "js",
        "css",
        "csv",
        "db",
        "xlsx",
        "pptx"
    )
    FLASK_ENV = "Development"
    LOG_FOLDER = os.path.join(basedir, "logs")
    STATIC_FOLDER = os.path.join(basedir, "static")
    IMG_UPLOAD_FOLDER = os.path.join(STATIC_FOLDER, "uploads")
    IMG_UPLOAD_URL = "/static/uploads"

    THREADS_PER_PAGE = 2
    REMEMBER_COOKIE_DURATION = timedelta(days=90)
    # prod
    # dev
    # SQLALCHEMY_DATABASE_URI = "postgresql://ridiculaptop:LeadPiggy2020!@localhost:5432/dev_db"
    SQLALCHEMY_ENGINE_OPTIONS = {
        "echo": False,
        "future": True,
    }

    LANGUAGES = {
        "en": {"flag": "us", "name": "English"},
        "es": {"flag": "es", "name": "Spanish"},
    }

    UPLOAD_FOLDER = os.path.join(STATIC_FOLDER, "uploads")

    WTF_CSRF_ENABLED = False
    # folder_locations
    DATA_FOLDER = os.path.join(STATIC_FOLDER, "data")

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class ProductionConfig(Config):
    DEBUG = False
    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600000

    # PostgreSQL database


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {"Production": ProductionConfig, "Development": DebugConfig}
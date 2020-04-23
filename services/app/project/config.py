"""Project general configurataion"""

import os


class Config:
    """Flask configuration"""

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = "xND4o83AFZTuax4dfde3452"

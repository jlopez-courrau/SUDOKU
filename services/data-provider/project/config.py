import os

basedir = os.path.abspath(os.path.dirname(__file__))

# add db informetion here

class Config:
    """TODO: this will change"""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")

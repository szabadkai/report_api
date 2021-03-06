import os


class Config:
    ENV = 'DEV'
    SQLALCHEMY_DATABASE_URI = os.environ.get("database_uri")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

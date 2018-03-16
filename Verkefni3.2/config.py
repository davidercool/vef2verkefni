import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DB_SOURCE_FILE = "data.sqlite"
    SECRET_KEY = "bueno"
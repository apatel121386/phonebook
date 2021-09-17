import os

basedir = os.path.abspath(os.path.dirname(__file__))

class config():
    SECRET_KEY = 'The-World-Is-Not-Enough'
    FLASK_APP = 'run'
    FLASK_ENV = os.environ.get('FLASK_ENV')
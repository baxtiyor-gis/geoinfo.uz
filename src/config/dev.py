from os.path import abspath, dirname
import os



DEBUG = True

HOST = "0.0.0.0"
PORT = 5000

SECRET_KEY = "secret"
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

CKEDITOR_PKG_TYPE = 'standard '
WTF_CSRF_SECRET_KEY = 'a random string'






basedir = abspath(dirname(dirname(__file__)))

CKEDITOR_SERVE_LOCAL= True
CKEDITOR_HEIGHT = 400

CKEDITOR_FILE_UPLOADER = 'upload'


CKEDITOR_ENABLE_CSRF= True


UPLOADED_PATH = os.path.join(basedir, 'uploads', 'ckeditor')

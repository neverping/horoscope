# General settings for each environment.
from tutorial.settings import *

DB_ENGINE = 'django.db.backends.sqlite3'
DB_NAME = '/opt/tutorial/db.sqlite3'
DB_USER = None
DB_PASS = None
DB_HOST = None
DB_PORT = None

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': DB_PORT
    }
}

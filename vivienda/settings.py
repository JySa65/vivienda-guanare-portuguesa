from vivienda.local_settings import *
import os
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

MIDDLEWARE += [
     'whitenoise.middleware.WhiteNoiseMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vivienda',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
from vivienda.local_settings import *
import os
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ['*']

MIDDLEWARE += [
     'whitenoise.middleware.WhiteNoiseMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vivienda',
        'USER': 'postgres',
        'PASSWORD': 'jysa',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
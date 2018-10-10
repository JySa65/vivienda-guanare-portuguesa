from vivienda.local_settings import *
import dj_database_url

DEBUG = False

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'vivienda',
#         'USER': 'postgres',
#         'PASSWORD': 'jysa',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


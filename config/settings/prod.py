from .base import *

ALLOWED_HOSTS = ['15.165.0.93']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'dGgP*M-_1u=c~3l3%!Zm!I;W3BTUd<=1',
        'HOST': 'ls-64e26c6527822661a675203898e9bb4af364831c.c4cpk7zjfjst.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432'
    }
}
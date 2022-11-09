from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-t8p(ftasdmfsdfd;krkt3!#@$4$o)##oeg4m^tt('

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '176.96.243.121']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'epihelp',
        'USER': 'epi',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
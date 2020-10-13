import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'xe%pk6kn3$va9g83n#uwskkx3wfvq=i_iuhk+r+qidh97b9#^y'


DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'movie',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'POST': '5432',
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'static')

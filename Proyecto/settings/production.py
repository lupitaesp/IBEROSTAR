from .base import *

#ARXHIVO QUE CONTIENE LA BASE DE DATOS Y SE VA A UTILIZAR CUANDO ESTEMOS EN MODO PRODUCCION
DEBUG = True

ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
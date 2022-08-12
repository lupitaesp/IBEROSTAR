from .base import *
DEBUG = True
#Archivo con la configuracion de la bd para cuando trabajaemos localmente 
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
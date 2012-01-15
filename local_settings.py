import os
from conf.settings.dev import *

DATABASES = { 
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'around-landing',
        'USER': 'sumoergo',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

PROJECT_DIR = os.sep.join(['home', 'sumoergo', 'projects', 'landing-around',
    'around_landing'])
TEMPLATE_DIRS = (
        '/home/sumoergo/projects/landing-around/around_landing/templates/',
)
STATIC_ROOT = os.sep.join([PROJECT_DIR, '..', 'static'])
STATICFILES_DIRS = (
            os.sep.join([PROJECT_DIR, '..', 'static']),
        )
MEDIA_ROOT = os.sep.join([PROJECT_DIR, '..', 'uploads'])

# For django.wsgi
SITE_DIR = PROJECT_DIR

# For AWS API access
AWS_ACCESS_KEY_ID = 'AKIAJFF5RZDAFLK6ADEQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'dev-around-assets'
AWS_DB_BACKUP_BUCKET_NAME = 'dev-around-assets'



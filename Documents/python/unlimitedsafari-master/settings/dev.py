"""
    this module holds the settings for development specific
    databases and such.
"""
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'unlimited_safari_devdb',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}

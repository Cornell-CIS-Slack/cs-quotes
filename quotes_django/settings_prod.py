"""
Django settings for quotes_django project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# Load the secret key from a file, which is never committed to version control 
with open(os.path.join(BASE_DIR, 'quotes_django/secret_key.txt')) as keyfile:
	SECRET_KEY = keyfile.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

# List of strings representing domain names this Django installation can serve
ALLOWED_HOSTS = ['quotes.cs.cornell.edu']

ADMINS = (('Edward', 'edward@cs.cornell.edu'))

import logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
		

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bleach',
    'quotespage',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'quotes_django.urls'

WSGI_APPLICATION = 'quotes_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Database password is also stored in a file, so it is never committed to version control
with open(os.path.join(BASE_DIR, 'quotes_django/db_pw.txt')) as pwfile:
	db_password = pwfile.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'quotes',
	'USER': 'ejt64',
	'PASSWORD': db_password,
	'HOST': '/extra/mysql/var/mysql.sock',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/extra/www/html/quotes/public_html/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/extra/www/html/quotes/public_html/media'

# Templates

TEMPLATE_DIRS = (
		os.path.join(BASE_DIR, 'templates'),
)

# Bleach settings

# Which HTML tags are allowed
BLEACH_ALLOWED_TAGS = ['p', 'b', 'i', 'u', 'em', 'strong', 
		'sup', 'sub', 'span']

# Which HTML attributes are allowed
BLEACH_ALLOWED_ATTRIBUTES = ['style']

# Which CSS properties are allowed in 'style' attributes (assuming
# style is an allowed attribute)
BLEACH_ALLOWED_STYLES = ['font-family', 'font-weight', 
		'text-decoration', 'font-variant']

# Strip unknown tags if True, replace with HTML escaped characters if
# False
BLEACH_STRIP_TAGS = True

# Strip comments, or leave them in.
BLEACH_STRIP_COMMENTS = False

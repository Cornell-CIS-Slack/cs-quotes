"""
Django settings for quotes_django project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Load the secret key from a file, which is never committed to version control 
with open(os.path.join(BASE_DIR, 'quotes_django/secret_key.txt')) as keyfile:
	SECRET_KEY = keyfile.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# List of strings representing domain names this Django installation can serve
ALLOWED_HOSTS = ['quotes.cs.cornell.edu']

ADMINS = [('Edward', 'edward@cs.cornell.edu')]

SERVER_EMAIL = 'root@quotes.cs.cornell.edu'

DEFAULT_FROM_EMAIL = 'webmaster@quotes.cs.cornell.edu'

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
	'django_cron',
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
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

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

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/extra/www/html/quotes/public_html/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/extra/www/html/quotes/public_html/media'

# Templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'), # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

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

# Django-cron settings

CRON_CLASSES = [
		'quotespage.crons.AdminApprovalEmailJob',
]

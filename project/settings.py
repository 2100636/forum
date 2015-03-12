"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the core like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9#fbu)(y(i7ochb)7j41!%te7l%p!utmx!svb^v*9$x^awd*yg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'project',
    'project.core',
    'south',
    'pybb',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.request',
	'django.contrib.messages.context_processors.messages',
    'pybb.context_processors.processor',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'pybb.middleware.PybbMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'forum',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'balabas',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        # 'TEST_CHARSET': 'UTF8',
        # 'TEST_DEPENDENCIES': ['slave'],
        # 'TEST_DEPENDENCIES': [],
        # 'TEST_MIRROR': 'slave',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
SITE_ID = 1
SITE_NAME = _(u'Test site')

TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

ugettext = lambda s: s

LANGUAGE_CODE = 'ru'
#
LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
    ('uk', 'Ukrainian'),
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

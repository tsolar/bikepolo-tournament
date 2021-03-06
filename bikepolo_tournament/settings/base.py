# coding: utf-8
import os.path

import django.conf.global_settings as DEFAULT_SETTINGS

# Django settings for bikepolo_tournament project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# here() gives us file paths from the root of the system to the directory
# holding the current file.
here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

PROJECT_ROOT = here("..")
# root() gives us file paths from the root of the system to whatever
# folder(s) we pass it starting at the parent directory of the current file.
root = lambda *x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)

ADMINS = (
    ('Tomás Solar', 'tsolar@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'bpt', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        # 'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        # 'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Santiago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 2

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# MEDIA_ROOT = ''
MEDIA_ROOT = root('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = ''
STATIC_ROOT = root('static') + '/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#STATIC_URL = 'https://s3.amazonaws.com/bikepolo_tournament-www/'
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    root('assets'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xxxxxxx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bikepolo_tournament.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'bikepolo_tournament.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates"
    # or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    root('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    # ...
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    # ...
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static', )

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    # 'social_auth',
    'south',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    # 'allauth.socialaccount.providers.bitly',
    # 'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.openid',
    # 'allauth.socialaccount.providers.persona',
    # 'allauth.socialaccount.providers.soundcloud',
    # 'allauth.socialaccount.providers.stackexchange',
    # 'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.vimeo',
    # 'allauth.socialaccount.providers.weibo',
)

LOCAL_APPS = (
    'base',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
#
# AUTHENTICATION_BACKENDS = (
#     'social_auth.backends.twitter.TwitterBackend',
#     'social_auth.backends.facebook.FacebookBackend',
#     # 'social_auth.backends.google.GoogleOAuthBackend',
#     'social_auth.backends.google.GoogleOAuth2Backend',
#     # 'social_auth.backends.google.GoogleBackend',
#     # 'social_auth.backends.yahoo.YahooBackend',
#     # 'social_auth.backends.browserid.BrowserIDBackend',
#     # 'social_auth.backends.contrib.linkedin.LinkedinBackend',
#     # 'social_auth.backends.contrib.disqus.DisqusBackend',
#     # 'social_auth.backends.contrib.livejournal.LiveJournalBackend',
#     # 'social_auth.backends.contrib.orkut.OrkutBackend',
#     # 'social_auth.backends.contrib.foursquare.FoursquareBackend',
#     # 'social_auth.backends.contrib.github.GithubBackend',
#     # 'social_auth.backends.contrib.vk.VKOAuth2Backend',
#     # 'social_auth.backends.contrib.live.LiveBackend',
#     # 'social_auth.backends.contrib.skyrock.SkyrockBackend',
#     # 'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
#     # 'social_auth.backends.contrib.readability.ReadabilityBackend',
#     # 'social_auth.backends.contrib.fedora.FedoraBackend',
#     # 'social_auth.backends.OpenIDBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)


try:
    from .social_auth_config import *
except ImportError:
    print('Falta la config para social auth')

SOCIALACCOUNT_PROVIDERS = \
    { 'facebook':
        { 'SCOPE': ['email'],
          'AUTH_PARAMS': { 'auth_type': 'reauthenticate' },
          'METHOD': 'oauth2' ,
          #'LOCALE_FUNC': 'path.to.callable'
        }
    }
# coding: utf-8

from __future__ import unicode_literals

import os
import socket


def get_profile():
    DEV_PROFILE = ''
    if os.path.exists('/Users'):                DEV_PROFILE = 'local'
    if os.path.exists('/home/vagrant'):        DEV_PROFILE = 'local'
    if socket.gethostname() == 'prob-preview':    DEV_PROFILE = 'preview'
    if socket.gethostname() == 'prob-django':    DEV_PROFILE = 'master'
    if socket.gethostname() == 'prob-d2':        DEV_PROFILE = 'master'
    return DEV_PROFILE


def hyphenate(s):
    return s.replace('_', '-')


PB_TITLE = 'Acamar web'
PB_PROJECT = 'acamar_web'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PB_PROJECT_IN_URL = hyphenate(PB_PROJECT)

DEV_PROFILE = get_profile()

if DEV_PROFILE == 'local':
    FILER_DEBUG = True
    DEBUG = True
    EMAIL_HOST = 'smtp.liten.cz'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME':   PB_PROJECT,
            'USER':   'root'
        }
    }
    STATIC_GRUNT_DIR = 'static-preview'
    BASE_URL = 'http://127.0.0.1:8000'
    RAVEN_ENABLED = False

elif DEV_PROFILE == 'preview':
    FILER_DEBUG = True
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.mysql',
            'NAME':     PB_PROJECT,
            'USER':     PB_PROJECT,
            'PASSWORD': '',
        }
    }
    STATIC_GRUNT_DIR = 'static-preview'
    BASE_URL = 'https://%s.preview.proboston.net' % hyphenate(PB_PROJECT)
    RAVEN_ENABLED = False

elif DEV_PROFILE == 'master':
    FILER_DEBUG = False
    DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.mysql',
            'NAME':     PB_PROJECT,
            'USER':     PB_PROJECT,
            'PASSWORD': '',
        }
    }
    STATIC_GRUNT_DIR = 'static-master'
    BASE_URL = 'https://%s.django2.proboston.net' % hyphenate(PB_PROJECT)
    RAVEN_ENABLED = True

RAVEN_DSN = 'https://a2d7d21344ab436b86c143d7aa9b9dc3:604a6dc004454286abaa1b3b2d9a23e5@sentry.io/1241537'

ALLOWED_HOSTS = ['p%s.django2.proboston.net' % hyphenate(PB_PROJECT), '127.0.0.1', 'localhost']

INSTALLED_APPS = (
    'djangocms_admin_style',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'cms',
    'menus',
    'treebeard',
    'sekizai',

    'filer',
    'easy_thumbnails',
    'mptt',
    'djangocms_text_ckeditor',

    'webpack_loader',
    'raven.contrib.django.raven_compat',

    'acamar_web'
)

MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, PB_PROJECT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings'
            ],
        },
    },
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'acamar_web.finders.GruntDirectoriesFinder'
)

CMS_TEMPLATES = [
    ('basic.html', 'Basic page template')
]

ROOT_URLCONF = '%s.urls' % PB_PROJECT
WSGI_APPLICATION = '%s.wsgi.application' % PB_PROJECT

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

if RAVEN_ENABLED:
    import raven

    release = 'development'
    try:
        release = raven.fetch_git_sha(os.path.dirname(os.path.dirname(__file__)))
    except raven.exceptions.InvalidGitRepository:
        pass

    RAVEN_CONFIG = {
        'dsn': RAVEN_DSN,
        'release': release,
    }

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                          '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',  # To capture more than ERROR, change to WARNING, INFO, etc.
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'sentry_exception': {
                'level': 'DEBUG',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.exception': {
                'level': 'DEBUG',
                'handlers': ['sentry_exception'],
                'propagate': False,
            },
        },
    }
else:
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
                'filters': (),
                'class': 'django.utils.log.AdminEmailHandler',
                'include_html': True
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True
            },
        }
    }

EMAIL_SUBJECT_PREFIX = 'DJANGO [%s/%s] ' % (PB_PROJECT, DEV_PROFILE)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
SECRET_KEY = '*-lra2%t^2z^gs2fbf+&ij_vo2c4nx-v%!kg^f27a!g2l#(2bm'

SITE_ID = 1
LANGUAGES = [
    ('cs', 'Čeština'),
    ('en', 'English'),
    ('ru', 'русский')
]
LANGUAGE_CODE = 'cs'
TIME_ZONE = 'Europe/Prague'

# uncomment to enable TZ support
USE_TZ = True
USE_I18N = True
USE_L10N = True

MANAGERS = ADMINS = (
    ('Jirka Makarius', 'jiri.makarius@proboston.net'),
)

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': PB_PROJECT + '/',  # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR,
                                   'webpack-stats-master.json') if STATIC_GRUNT_DIR == "static-master" else os.path.join(
            BASE_DIR, 'webpack-stats-preview.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

if DEV_PROFILE != 'local':
    import urllib2

    proxy_support = urllib2.ProxyHandler({"http": "http://localhost:8888", "https": "http://localhost:8888"})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)


if os.path.exists(os.path.join(BASE_DIR, 'settings.local.py')):
    from settings.local import *
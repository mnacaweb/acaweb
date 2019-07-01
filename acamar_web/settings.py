# coding: utf-8


import os
import socket


def get_profile():
    DEV_PROFILE = ""
    if os.path.exists("/Users"):
        DEV_PROFILE = "local"
    if os.path.exists("/usr/src/app"):
        DEV_PROFILE = "local"
    if socket.gethostname() == "prob-prev":
        DEV_PROFILE = "preview"
    if socket.gethostname() == "prob-django":
        DEV_PROFILE = "master"
    if socket.gethostname() == "prob-prod":
        DEV_PROFILE = "master"
    return DEV_PROFILE


def hyphenate(s):
    return s.replace("_", "-")


CMS_PAGE_CACHE = False
CMS_PLACEHOLDER_CACHE = False
CMS_PLUGIN_CACHE = False

PB_TITLE = "Acamar web"
PB_PROJECT = "acamar_web"
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PB_PROJECT_IN_URL = hyphenate(PB_PROJECT)

DEV_PROFILE = get_profile()

IN_DOCKER = os.path.exists("/usr/src/app")

if DEV_PROFILE == "local":
    FILER_DEBUG = True
    DEBUG = True
    EMAIL_HOST = "smtp.liten.cz"
    DATABASES = {
        "default": {
            "HOST": "db" if IN_DOCKER else "",
            "ENGINE": "django.db.backends.mysql",
            "NAME": PB_PROJECT,
            "USER": "root",
        }
    }
    STATIC_GRUNT_DIR = "static-preview"
    BASE_URL = "http://127.0.0.1:8000"
    RAVEN_ENABLED = False

elif DEV_PROFILE == "preview":
    FILER_DEBUG = True
    DEBUG = True
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": PB_PROJECT,
            "USER": PB_PROJECT,
            "PASSWORD": "sNfCCb1T"
            # "PASSWORD": "GAzwyTUeH",
        }
    }
    STATIC_GRUNT_DIR = "static-preview"
    BASE_URL = "https://%s.prob-prev.glow.cz" % hyphenate(PB_PROJECT)
    RAVEN_ENABLED = True
    DEPLOYED_ON = "prob-prev"

elif DEV_PROFILE == "master":
    FILER_DEBUG = False
    DEBUG = False
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": PB_PROJECT,
            "USER": PB_PROJECT,
            "PASSWORD": "mxd33LHjoz",
        }
    }
    STATIC_GRUNT_DIR = "static-master"
    BASE_URL = "https://acamar.cz"
    RAVEN_ENABLED = False
    DEPLOYED_ON = "prob-prod"

RAVEN_DSN = "https://a2d7d21344ab436b86c143d7aa9b9dc3:604a6dc004454286abaa1b3b2d9a23e5@sentry.io/1241537"

# ALLOWED_HOSTS = [
#     "www.acamar.cz",
#     "acamar.cz",
#     "%s.django2.proboston.net" % hyphenate(PB_PROJECT),
#     "%s.prob-prev.glow.cz" % hyphenate(PB_PROJECT),
#     "%s.prob-prod.glow.cz" % hyphenate(PB_PROJECT),
#     "127.0.0.1",
#     "localhost",
# ]
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    "djangocms_admin_style",
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sites",
    "cms",
    "menus",
    "treebeard",
    "sekizai",
    "filer",
    "easy_thumbnails",
    "mptt",
    "djangocms_text_ckeditor",
    "meta",
    "djangocms_page_meta",
    "adminsortable",
    "django_extensions",
    "haystack",
    "safedelete",
    "django_crontab",
    "rosetta",
    "webpack_loader",
    "acamar_api",
    "acamar_web",
)

MIDDLEWARE = (
    # "django.middleware.cache.UpdateCacheMiddleware",
    # "cms.middleware.utils.ApphookReloadMiddleware",
    # "django.contrib.sessions.middleware.SessionMiddleware",
    # "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    # "django.contrib.auth.middleware.AuthenticationMiddleware",
    # "django.contrib.messages.middleware.MessageMiddleware",
    # "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "django.middleware.security.SecurityMiddleware",
    # "django.middleware.locale.LocaleMiddleware",
    # "cms.middleware.user.CurrentUserMiddleware",
    # "cms.middleware.page.CurrentPageMiddleware",
    # "cms.middleware.toolbar.ToolbarMiddleware",
    # "cms.middleware.language.LanguageCookieMiddleware",
    # "django.middleware.cache.FetchFromCacheMiddleware",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, PB_PROJECT, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.template.context_processors.i18n",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
                "cms.context_processors.cms_settings",
                "acamar_web.context_processors.project_settings",
                "acamar_web.context_processors.site",
            ]
        },
    }
]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "acamar_web.finders.GruntDirectoriesFinder",
)

LOGIN_URL = "api:login"
LOGIN_REDIRECT_URL = "/"

CMS_PERMISSION = True
CMS_TEMPLATE_INHERITANCE = False
CMS_TEMPLATES = [
    ('basic.html', 'Basic page template'),
    ('we_are.html', 'We are'),
    ('contact.html', 'Contact'),
    ('for_candidates.html', 'For candidates'),
    ('for_companies.html', 'For companies'),
    ('course.html', 'Courses'),
    ('a-card.html', 'A-card'),
    ('enroll_in_course.html', 'Enroll in course'),
    ('thank_you.html', 'Thank you'),
    ('privacy-policy.html', 'Privacy policy'),
]

ROOT_URLCONF = "%s.urls" % PB_PROJECT
WSGI_APPLICATION = "%s.wsgi.application" % PB_PROJECT

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

DEFAULT_FROM_EMAIL = "no-reply-acamar-web@proboston.net"

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

FILER_FILE_MODELS = ("acamar_web.FilerVideo", "filer.Image", "filer.File")

CKEDITOR_SETTINGS = {
    "language": "{{ language }}",
    "toolbar_CMS": [
        ["Undo", "Redo"],
        ["cmsplugins", "-", "ShowBlocks"],
        ["Format", "Styles"],
    ],
    "toolbar_HTMLField": [["Undo", "Redo"], ["ShowBlocks"], ["Format", "Styles"]],
    "skin": "moono-lisa",
}

CKEDITOR_SETTINGS_TEXT = {
    "disallowedContent": "h1 h2 h3",
    "toolbar_HTMLField": [
        ["Undo", "Redo"],
        ["ShowBlocks"],
        ["Styles"],
        [
            "Bold",
            "Italic",
            "Underline",
            "-",
            "Subscript",
            "Superscript",
            "-",
            "RemoveFormat",
        ],
    ],
}

META_SITE_PROTOCOL = "http"
META_USE_SITES = True
META_SITE_TYPE = "website"
META_SITE_NAME = "Acamar"
META_INCLUDE_KEYWORDS = []
META_DEFAULT_KEYWORDS = []
META_USE_OG_PROPERTIES = False
META_USE_TWITTER_PROPERTIES = False
META_USE_GOOGLEPLUS_PROPERTIES = False

ELASTIC_URL = ("http://elastic:9200" if IN_DOCKER else "http://localhost:9200/") if DEV_PROFILE == "local" else "http://prob-elastic:9200/"

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "acamar_web.search.engine.Elasticsearch5SearchEngineCz",
        "URL": ELASTIC_URL,
        "INDEX_NAME": "{}_{}_haystack".format(PB_PROJECT, "cz"),
    },
    "default_en": {
        "ENGINE": "haystack.backends.elasticsearch5_backend.Elasticsearch5SearchEngine",
        "URL": ELASTIC_URL,
        "INDEX_NAME": "{}_{}_haystack".format(PB_PROJECT, "en"),
    },
    "default_ru": {
        "ENGINE": "acamar_web.search.engine.Elasticsearch5SearchEngineRu",
        "URL": ELASTIC_URL,
        "INDEX_NAME": "{}_{}_haystack".format(PB_PROJECT, "ru"),
    },
}

HAYSTACK_ROUTERS = ["acamar_web.search.router.LanguageRouter"]
HAYSTACK_SIGNAL_PROCESSOR = "acamar_web.search.signals.PositionRealtimeSignalProcessor"

CRONJOBS = [
    (
        "0 * * * *",
        "django.core.management.call_command",
        ["sync_positions"],
        {},
        ">> {}".format(os.path.join(BASE_DIR, "logs", "sync_positions.log")),
    ),
    (
        "30 0 * * *",
        "django.core.management.call_command",
        ["rebuild_index", "--noinput"],
        {},
        ">> {}".format(os.path.join(BASE_DIR, "logs", "sync_positions.log")),
    ),
]

EMAIL_SUBJECT_PREFIX = "DJANGO [%s/%s] " % (PB_PROJECT, DEV_PROFILE)
DEFAULT_FROM_EMAIL = "no-reply@services.acamar.cz"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
SECRET_KEY = "*-lra2%t^2z^gs2fbf+&ij_vo2c4nx-v%!kg^f27a!g2l#(2bm"

SITE_ID = 1
LANGUAGES = [("cs", "Čeština"), ("en", "English"), ("ru", "русский")]
LANGUAGE_CODE = "cs"
LANGUAGES_VERBOSE = {"cs": "CZ", "en": "EN", "ru": "RU"}
ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = "cs"
ROSETTA_SHOW_AT_ADMIN_PANEL = True

TIME_ZONE = "Europe/Prague"

# uncomment to enable TZ support
USE_TZ = True
USE_I18N = True
USE_L10N = True
MODELTRANSLATION_DEBUG = False
# MODELTRANSLATION_DEFAULT_LANGUAGE = "cs"

MANAGERS = ADMINS = (
    ("Jirka Makarius", "jiri.makarius@proboston.net"),
    ("Lukas Sova", "lukas.sova@proboston.net"),
    ("Lukas 2", "lukas@ornyx.com")
)

CMS_PLACEHOLDER_CONF = {
    "main_banner": {
        "plugins": ["MainBannerPlugin"],
        "name": "Main Banner",
        "limits": {"MainBannerPlugin": 1, "MainBannerCardPlugin": 2},
        "default_plugins": [
            {"plugin_type": "MainBannerPlugin", "values": {"title": ""}}
        ],
    },
    "basic": {
        "plugins": [
            "WorkElipsePlugin",
            "ReviewPanelPlugin",
            "LogoPanelPlugin",
            "CoursePanelPlugin",
        ],
        "name": "Content",
    },
    "we_are": {
        "plugins": ["CreateTeamPlugin", "TeamGridPlugin", "LogoPanelPlugin"],
        "name": "Content - we are",
    },
    "contact": {
        "plugins": ["ContactGridPlugin", "ContactFormPlugin", "MapPlugin"],
        "name": "Content - contact",
    },
    "for_candidates": {
        "plugins": [
            "PositionSearchPlugin",
            "QuotePlugin",
            "BubblePanelPlugin",
            "TimelinePlugin",
            "AcaFriendPanelPlugin",
            "ContactUsPlugin",
        ],
        "name": "Content - for candidates",
    },
    "for_companies": {
        "plugins": [
            "GraphSectionPlugin",
            "PartnersPlugin",
            "TimelinePlugin",
            "ContactPersonPlugin",
        ],
        "name": "Content - for companies",
    },
    "course": {
        "plugins": [
            "CreateTeamPlugin",
            "CoursePanelPlugin",
            "CourseLectorPlugin",
            "AcaFriendPanelPlugin",
            "TimelinePlugin",
            "ContactPersonPlugin",
        ],
        "name": "Content - course",
    },
    "a-card": {
        "plugins": ["AcardBenefitsPlugin", "LoginPlugin"],
        "name": "Content A-card",
    },
    "course_content": {
        "plugins": [
            "CourseBasicInfoPlugin",
            "CourseBonusPanelPlugin",
            "CourseProgramPlugin",
            "CoursePanelPlugin",
            "CourseTermListPlugin",
            "CourseGenericRegistrationPlugin",
            "ContactPersonPlugin",
        ],
        "name": "Course detail content",
    },
    "enroll_in_course": {
        "plugins": ["CourseEnrollFormPlugin", "TimelinePlugin"],
        "name": "Content - enroll in course",
        "limits": {"CourseEnrollFormPlugin": 1, "TimelinePlugin": 1},
    },
    "thank_you": {
        "plugins": ["ThanksBannerPlugin"],
        "name": "Content - thank you",
        "limits": {"global": 1},
    },
}

WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": PB_PROJECT + "/",  # must end with slash
        "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats-master.json")
        if STATIC_GRUNT_DIR == "static-master"
        else os.path.join(BASE_DIR, "webpack-stats-preview.json"),
        "POLL_INTERVAL": 0.1,
        "TIMEOUT": None,
        "IGNORE": [".+\.hot-update.js", ".+\.map"],
    }
}

PROXIES = (
    {"http": "http://localhost:8888", "https": "http://localhost:8888"}
    if DEV_PROFILE != "local"
    else {}
)

if RAVEN_ENABLED:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(dsn=RAVEN_DSN, integrations=[DjangoIntegration()], http_proxy=PROXIES.get("http"))

else:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}
        },
        "handlers": {
            "mail_admins": {
                "level": "ERROR",
                "filters": ("require_debug_false",),
                "class": "django.utils.log.AdminEmailHandler",
                "include_html": True,
            },
            # 'file': {
            #     'level': 'ERROR',
            #     "filters": ("require_debug_false",),
            #     'class': 'logging.FileHandler',
            #     'filename': os.path.join(BASE_DIR, 'log', 'debug.log'),
            # }
        },
        "loggers": {
            "django.request": {
                "handlers": ["mail_admins"],
                "level": "ERROR",
                "propagate": True,
            }
        },
    }

if DEV_PROFILE != "local":
    import urllib.request, urllib.error, urllib.parse

    proxy_support = urllib.request.ProxyHandler(PROXIES)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    # CACHES = {
    #     "default": {
    #         "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
    #         "LOCATION": "127.0.0.1:11211",
    #     }
    # }
    TEST_RUNNER = "acamar_web.test.testrunner.NoDbTestRunner"

if os.path.exists(os.path.join(BASE_DIR, "acamar_web", "settings_local.py")):
    from .settings_local import *

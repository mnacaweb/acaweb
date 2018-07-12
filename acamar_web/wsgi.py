"""
WSGI config for acamar_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from raven.contrib.django.middleware.wsgi import Sentry

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acamar_web.settings")

application = get_wsgi_application()

# uWSGI
# if settings.DEV_PROFILE != 'local':
#     application({
#         'REQUEST_METHOD': 'GET',
#         'SERVER_NAME': '127.0.0.1',
#         'SERVER_PORT': 80,
#         'PATH_INFO': '/cs/',
#         'REMOTE_ADDR': '127.0.0.1',
#         'wsgi.input': sys.stdin,
#     }, lambda x, y: None)

application = Sentry(application)

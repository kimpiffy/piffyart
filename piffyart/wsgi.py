"""WSGI config for piffyart project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "piffyart.settings")

application = get_wsgi_application()

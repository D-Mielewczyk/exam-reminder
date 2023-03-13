"""
WSGI config for exam_reminder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'azureproject.production' if 'WEBSITE_HOSTNAME' in os.environ else 'azureproject.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exam_reminder.settings')

application = get_wsgi_application()

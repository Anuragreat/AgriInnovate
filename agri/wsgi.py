"""
WSGI config for agri project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise

from django.core.wsgi import get_wsgi_application

application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agri.settings')

application = get_wsgi_application()

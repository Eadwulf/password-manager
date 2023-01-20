import os
import django


def setup_django(): 
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    django.setup()
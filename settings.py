###############################################################################
# Django Standalone ORM Settings File
# Used for accessing Django ORM without running a web server.
###############################################################################

import os
from pathlib import Path

# Build paths
BASE_DIR = Path(__file__).resolve().parent

# SECRET_KEY is required even when not running a web server
SECRET_KEY = 'standalone-django-orm-key'

# Installed apps for this project
# ONLY include the db app (your models live here)
INSTALLED_APPS = [
    'db',
]

# Database configuration (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database.sqlite3',
    }
}

# Required Django settings for ORM usage
# (even though no templates or middleware are needed)
USE_TZ = True
TIME_ZONE = 'UTC'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


import dj_database_url
from pathlib import Path
import os 
from .base import *

print("prod settings loaded")


SECRET_KEY = os.environ.get("SECRET_KEY") 


DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


database_url = os.environ.get("DATABASE_URL")

DATABASES["default"] = dj_database_url.parse("postgresql://db_messaround_user:ChQ81JOdIj0QWJyLt823vO9qaYa50lyM@dpg-crq6vb52ng1s73e3gjs0-a.frankfurt-postgres.render.com/db_messaround")
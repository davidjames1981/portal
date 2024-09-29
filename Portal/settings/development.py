
import dj_database_url
from pathlib import Path
import os 
from .base import *

print("Development settings loaded")


SECRET_KEY = '_m9gq*br^n-=j5-10&7mnq)0_dz04-)h#u_4hy(y8i56-@s)#x'

DEBUG = 'True'

ALLOWED_HOSTS = ["*"]


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


database_url = os.environ.get("DATABASE_URL")

DATABASES["default"] = dj_database_url.parse("postgresql://db_messaround_user:ChQ81JOdIj0QWJyLt823vO9qaYa50lyM@dpg-crq6vb52ng1s73e3gjs0-a.frankfurt-postgres.render.com/db_messaround")
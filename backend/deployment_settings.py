import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

STORAGES = {
    "default":{
        "BACKEND" : "django.core.files.storage.FileSystemStorage",
    },
}

DATABASES = {
    'default':dj_database_url.config(
        default=os.environ['DATABASE_URL'],
        conn_max_age =600
    )
}
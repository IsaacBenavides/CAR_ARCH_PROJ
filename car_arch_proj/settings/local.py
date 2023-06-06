from .base import *


ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = []

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


STATIC_URL = "/static/"

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

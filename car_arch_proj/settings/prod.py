from .base import *

ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = []


STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

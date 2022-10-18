import environ

from .base import *  # noqa

config = environ.Env()
environ.Env.read_env(".env")

SECRET_KEY = config.str("SECRET_KEY", "This is not secret")

DEBUG = config.bool("DEBUG", True)

ALLOWED_HOSTS = config.list("ALLOWED_HOSTS", default=[])

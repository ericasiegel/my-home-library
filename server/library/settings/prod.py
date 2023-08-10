from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
import os


SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []
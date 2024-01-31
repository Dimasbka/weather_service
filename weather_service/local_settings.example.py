
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gu4stsz1lsz$4&hs_mg4@p+8k$94%^rv%dh7@nk&v!jtgu@a4='


# SECURITY WARNING: keep the secret key used in production secret!
# можно получить на официальном веб сайте developer.tech.yandex.ru/services 
YANDEX_API_KEY = "!!! enter your key !!!"
YANDEX_API_CACHE_TIME = 30*60 


# можно получить на сайте https://botostore.com/c/botfather/ 
BOT_URL = '!!! enter your bot url !!!'
BOT_TOKEN = '!!! enter your bot token !!!'

# Это адрес вашего сайта видимый из веба 
# на который будут приходить сообщения от телеграмма
BOT_WEBHOOK = "!!! enter your bot webhook addres !!!"
ALLOWED_HOSTS = [
    '!!! enter your bot webhook host !!!',
    '127.0.0.1',
]


LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'production': {
        'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'db.backends.postgresql_9_2',
        'NAME': 'weather_service',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5434',
        'CONN_MAX_AGE': 300,
    }
}

# https://docs.djangoproject.com/en/4.2/topics/cache/
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'production': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

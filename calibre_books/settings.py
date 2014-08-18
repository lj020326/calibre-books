import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = bool(os.environ.get('DEBUG', False))

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split()


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'calibre_books.core',
    'calibre_books.calibre',

    # External apps
    'bootstrap3',
    'raven.contrib.django.raven_compat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'sslify.middleware.SSLifyMiddleware',
)

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates')
]

ROOT_URLCONF = 'calibre_books.urls'

WSGI_APPLICATION = 'calibre_books.wsgi.application'


SQLITE_DB_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': dj_database_url.config(default=SQLITE_DB_URL),
    'calibre': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'metadata.db'),
    }
}

DATABASE_ROUTERS = ['calibre_books.calibre.db_router.DbRouter']

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'calibre_books', 'static'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SSLIFY_DISABLE = bool(os.environ.get('SSLIFY_DISABLE', False))

DROPBOX_CONSUMER_KEY = os.environ.get('DROPBOX_CONSUMER_KEY')
DROPBOX_CONSUMER_SECRET = os.environ.get('DROPBOX_CONSUMER_SECRET')
DROPBOX_ACCESS_TOKEN = os.environ.get('DROPBOX_ACCESS_TOKEN')
DROPBOX_ACCESS_TOKEN_SECRET = os.environ.get('DROPBOX_ACCESS_TOKEN_SECRET')
DROPBOX_ACCESS_TYPE = 'dropbox'

DROPBOX_CALIBRE_DIR = 'CalibreLibrary'

RAVEN_CONFIG = {'dsn': os.environ.get('SENTRY_DSN', '')}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry']
    },
    'handlers': {
        'sentry': {
            'level': 'INFO',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'loggers': {
        'calibre_books': {
            'level': 'INFO',
            'handlers': ['sentry'],
            'propagate': False
        }
    }
}

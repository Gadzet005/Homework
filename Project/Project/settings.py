from pathlib import Path

from django.urls.base import reverse_lazy
from django_cleanup.signals import cleanup_pre_delete

from sorl.thumbnail import delete
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

environ.Env.read_env('.env')


SECRET_KEY = env.str('SECRET_KEY', default='This is not secret')

DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

INTERNAL_IPS = ['127.0.0.1']


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MODULE_APPS = [
    'django_cleanup.apps.CleanupConfig',
    'sorl.thumbnail',
    'ckeditor',
    'debug_toolbar'
]

LOCAL_APPS = [
    'Core',
    'Users.apps.UsersConfig',
    'homepage.apps.HomepageConfig',
    'catalog.apps.CatalogConfig',
    'about.apps.AboutConfig',
    'feedback.apps.FeedbackConfig',
    'rating.apps.RatingConfig'
]

INSTALLED_APPS = DJANGO_APPS + MODULE_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Users.context_processors.extras',
            ],
        },
    },
]

WSGI_APPLICATION = 'Project.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FIXTURE_DIRS = [
    BASE_DIR / 'fixtures'
    ]

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static_dev'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


THUMBNAIL_COLORSPACE = None
THUMBNAIL_PRESERVE_FORMAT = True


EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'
OWNER_EMAIL = env.str('OWNER_EMAIL', default='default@gmail.com')

AUTH_USER_MODEL = 'Users.User'
LOGIN_URL = reverse_lazy('users:login')
LOGIN_REDIRECT_URL = reverse_lazy('homepage:home')


# Очистка кэша sorl.thumbnail
def sorl_delete(**kwargs):
    delete(kwargs['file'])


cleanup_pre_delete.connect(sorl_delete)

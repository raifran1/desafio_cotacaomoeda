import os
import sys
from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configurando o path das apps como root

sys.path.insert(0, os.path.join(BASE_DIR, 'app'))
map(lambda directory: sys.path.insert(0, os.path.join(BASE_DIR, directory)), ['app'])

# SECURITY: Atualizar para uma chave
SECRET_KEY = 'django-insecure-@-^)837s6$tb=)9!hm(s^1jzoc-^d9z0ocpea%_%rz4ote2eyp'

# Ativa e desativa os logs de debug
DEBUG = config('DEBUG', cast=bool, default=False)

# Hosts habilitados
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')],
                       default='*')

INTERNAL_IPS = ['127.0.0.1', 'localhost:3000']

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'moeda',
    'cotacao_moeda',
    'website',
    'api',
]

INSTALLED_APPS = DJANGO_APPS + MY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cotacao.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cotacao.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME', default='cotacao'),
        'USER': config('DB_USER', default='root'),
        'PASSWORD': config('DB_PASSWORD', default='root'),
        'HOST': config('DB_HOST', default='127.0.0.1'),
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


# Password validation

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

SITE_ID = 1

SITE_URL = config('SITE_URL', default='')

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ORIGIN_ALLOW_ALL = True

SECURE_REFERRER_POLICY = None

X_FRAME_OPTIONS = 'SAMEORIGIN'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = config('STATIC_ROOT')
MEDIA_ROOT = config('MEDIA_ROOT')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

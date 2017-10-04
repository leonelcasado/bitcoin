# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os
import socket
import datetime
# ==============================================================
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ==============================================================
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_nt8y(i_7=0@nf7%epts(*hvz0ecrb^b)2gfhnizj&mci3=02s'
# ==============================================================
PASSWORD_DEFAULT='bitcoin'
# ==============================================================
# SECURITY WARNING: don't run with debug turned on in production!
#print '======================='
#print(socket.gethostname())
#print '======================='
if socket.gethostname() == "windows-PC":
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    NAME_DB= 'bitcoin'
    USER_DB= 'root'
    PASSWORD_DB= ''
    HOST_DB='localhost'

    STATIC_PATH = BASE_DIR+'\static'
    PATH_MEDIA_ROOT = BASE_DIR+'\media'
    PATH_MEDIA_URL = '/media/'
    CONEXAO='LOCAL'
else:
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    NAME_DB= 'clubebitcoin$hml_bitcoin'
    USER_DB= 'clubebitcoin'
    PASSWORD_DB= 'teste123456'
    HOST_DB='clubebitcoin.mysql.pythonanywhere-services.com'

    STATIC_PATH = BASE_DIR+'\static'
    PATH_MEDIA_ROOT = BASE_DIR+'\media'
    PATH_MEDIA_URL = '/media/'
    CONEXAO='HOMOLOGAÇÃO'
# ==============================================================
# Application definition
# ==============================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
]
INSTALLED_APPS += [
    'django_extensions',
    'simple_history',
    'rest_framework',
    'rest_framework_jwt',
]
INSTALLED_APPS += [
    'bitcoin.backend.historico',
    'bitcoin.backend.investidor',
]
# ==============================================================
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]
# ==============================================================
ROOT_URLCONF = 'bitcoin.urls'
# ==============================================================
#http://getblimp.github.io/django-rest-framework-jwt/
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=12),#seconds=60,minutes=5,hours=12
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': True, #False
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'Token',#JWT,Token
}
'''REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_jwt.authentication.JSONWebTokenAuthentication',),
}'''
# ==============================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
            'libraries': {
                'utils': 'bitcoin.backend.core.templatetags.utils',

            },
        },
    },
]
# ==============================================================
WSGI_APPLICATION = 'bitcoin.wsgi.application'
# ==============================================================
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
   'default': {
       
       'ENGINE': 'django.db.backends.mysql',
       'PORT': '3306',

       #'ENGINE': 'django.db.backends.postgresql_psycopg2',
       #'PORT': '5432',
       
       'NAME': NAME_DB,
       'USER': USER_DB,
       'PASSWORD': PASSWORD_DB,
       'HOST': HOST_DB,
   }
}
# ==============================================================
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
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
# ==============================================================
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
# ==============================================================
LANGUAGE_CODE = 'pt-br'
# ==============================================================
# https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
DATE_FORMAT = 'd/m/Y'
DATETIME_FORMAT = 'd/m/Y H:i:s'
SHORT_DATETIME_FORMAT = 'd/m/Y H:i'
SHORT_DATE_FORMAT = 'd/m'
TIME_FORMAT = 'H:i:s'
SHORT_TIME_FORMAT = 'H:i'
DATE_INPUT_FORMATS = ('%d/%m/%Y',)
TIME_INPUT_FORMATS = ('%H:%M',)
# ==============================================================
TIME_ZONE = 'America/Maceio'
USE_I18N = True
USE_L10N = False #True
USE_TZ = False #True
# ==============================================================
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATICFILES_DIRS = [
    STATIC_PATH,
]
STATIC_URL = '/static/'
# ==============================================================
#MEDIA_ROOT = os.path.join(BASE_DIR,'apolomobi','backend','media')
MEDIA_ROOT = PATH_MEDIA_ROOT
MEDIA_URL = PATH_MEDIA_URL
# ==============================================================
#AUTH_USER_MODEL = 'usuario.Usuario'
#LOGIN_URL = 'usuario:login'
#LOGIN_REDIRECT_URL = 'usuario:login'
#LOGOUT_URL = 'usuario:logout'
# ==============================================================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'apolomobi@gmail.com'
EMAIL_HOST_PASSWORD = 'apolomobi2017'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# ==============================================================

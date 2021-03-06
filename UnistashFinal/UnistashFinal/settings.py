"""
Django settings for UnistashFinal project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

import smtplib
#import Functions.templatetags.myfilters.py
#import impsettings

SENDER='igdtunistash@gmail.com'
PASS= ''

GOOGLE_RECAPTCHA_SECRET_KEY = '6LffWSkUAAAAAJX3JOSvGQTVw9AY9egMZ5Dmrwhm'
EMAIL_HOST      = 'smtp.gmail.com' 
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = 'igdtunistash@gmail.com'
EMAIL_PORT      = 587
EMAIL_USE_TLS   = True
DEFAULT_FROM_EMAIL  = 'igdtunistash@gmail.com'
SERVER_EMAIL    = 'igdtunistash@gmail.com'
# for console
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


LOGIN_REDIRECT_URL = 'index.html'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8w803fn__v4rz%7!afoos^*4l%!yt0h_imcg3&%r$(*60@%3&-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #True #

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Functions',
    'captcha',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'UnistashFinal.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],


             'libraries':{
            'myfilters': 'Functions.templatetags.myfilters',

            }
        },
    },
]

WSGI_APPLICATION = 'UnistashFinal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'unistashfinal',
        'USER': 'root',
        'PASSWORD': 'system',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/static/',
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')

# and this is for the users on the browser
#while using in developer mode then use these urls further could be changed

MEDIA_URL ='/media/'
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

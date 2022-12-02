"""
Django settings for phonetic project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*d8db^%q@z=#itwhobaibx$sqnvz2=@2%$@t=h!c$9-4i716l9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ADMINS = (
     ('Pablo M', 'pabmargom3@alum.us.es'),
     ('Migueles', 'framigdom@alum.us.es'),
     ('Pablo A', 'pabalvcar@alum.us.es'),
     ('Diego R', 'dieruigil@alum.us.es'),
     ('David Z', 'davzamfer@alum.us.es'),
)

ALLOWED_HOSTS = ['127.0.0.1','localhost']
STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'principal/static/')
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'principal.apps.PrincipalConfig',
    'bootstrap4',
    
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'allauth.socialaccount.providers.google',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', 
    'allauth.account.auth_backends.AuthenticationBackend',
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

ROOT_URLCONF = 'phonetic.urls'

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

WSGI_APPLICATION = 'phonetic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-dark',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'

STRIPE_SECRET_KEY  = 'sk_test_51M9ulBDVy5OU3kBg96NyPjE09JdzdQwg2ZpFVyRpBncfhIcrSZzowQTTi8Otv7EmCqO0I0BelZ5mCwPk05EVDqXs007e3YwwR4'
STRIPE_PUBLIC_KEY = 'pk_test_51M9ulBDVy5OU3kBgBtXmlHyYxAMg0ju1VrSNQzFuJ1H5wGM46yWpbkLwTtD4eeo5w9EssPe12asHSYOLDtyDtBGs00BZZAAW3Z'

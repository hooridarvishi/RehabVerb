"""
Django settings for texapp project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&hby%a7a&sv#5cl4)v27@39+g8h!x5x(gguk=ig_sbtwuwx0jv"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "verbtherapy.apps.VerbtherapyConfig",
    "storages",
]
import os
AWS_S3_ENDPOINT_URL = os.getenv("ENDPOINT")
AWS_STORAGE_BUCKET_NAME = os.getenv("BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.getenv("ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("SECRET_KEY")
AWS_S3_OBJECT_PARAMETERS = {
  'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

BROKER_URL = 'redis://:<admin>@<services.irn2.chabokan.net>:<5432>/<database_number>'
CELERY_RESULT_BACKEND = 'redis://:<admin>@<>:<services.irn2.chabokan.net>/<database_number>'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Tehran'



MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "texapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "texapp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'myproject_aphasia',  # نام دیتابیس جدید
#         'USER': 'postgres',    # نام کاربری PostgreSQL
#         'PASSWORD': 'admin',  # پسوردی که در زمان نصب تعیین کرده‌اید
#         'HOST': 'services.irn2.chabokan.net',   # یا آدرس IP سرور
#         'PORT': '5432',        # پورت پیش‌فرض PostgreSQL
#     }
# }
import os
DATABASES = {
    'default': {
        'ENGINE': os.getenv("django.db.backends.postgresql"),
        'NAME': os.getenv("myproject_aphasia"),
        'USER': os.getenv("postgres"),
        'PASSWORD': os.getenv("admin"),
        'HOST': os.getenv("services.irn2.chabokan.net"),
        'PORT':  os.getenv("5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
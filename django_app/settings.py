"""
Django settings for django_app project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url # type: ignore

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-7=r!ivhy&=i3@3pal_1v$evp$bo&y%=#66y_+!7ucud(0d0-!='
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG",'False') == True # should be added if Debug is false

DEBUG = True# should be added if Debug is false



ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'accounts',
    'rest_framework',
    'corsheaders',
    'project',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # Add CORS middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', #used for session management
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_app.middleware.LogRequestMiddleware',  # Add custom middleware
    'django_app.middleware.CustomHeaderMiddleware',  # Add custom middleware
]

ROOT_URLCONF = 'django_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], #DIRS: A list of directories where the engine should look for template source files, in search order.
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

WSGI_APPLICATION = 'django_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', #ENGINE: Specifies the database backend (e.g., PostgreSQL, MySQL).
        'NAME': BASE_DIR / 'db.sqlite3', #NAME: The name of the database file (for SQLite).
    }
}
databaseURL = os.environ.get('DATABASE_URL')
DATABASES['default'] = dj_database_url.parse(databaseURL) 
# DATABASES['default'] = dj_database_url.parse('postgresql://polls_db_ucdy_user:hLlQEtoyUJv2nBivJA1pEnvwtVadEb8i@dpg-csa69qa3esus739pmr30-a.singapore-postgres.render.com/polls_db_ucdy') # This line of code is used to parse the database URL from the environment variable DATABASE_URL. This is useful when you deploy your Django application to Heroku, as Heroku automatically sets the DATABASE_URL environment variable for you. This line of code will parse the database URL and set the default database configuration for your Django application.
# The above code is the default database configuration that Django uses when you first create a project.

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default backend
    # Add custom backends if you're using any
]

#Login URL
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = 'polls:index'
LOGOUT_REDIRECT_URL = 'polls:index'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
     'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    'EXCEPTION_HANDLER': 'django_app.utils.custom_exception_handler',
}

CORS_ALLOWED_ORIGINS = [
    "https://my-portfolio-ui-beta.vercel.app/", 
]
CORS_ALLOW_CREDENTIALS = False  # Since we're not using cookies for authentication

CORS_ALLOW_ALL_ORIGINS = DEBUG #for dev purpose

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

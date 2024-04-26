"""
Django settings for xaamga_api project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(8rh@3k3in!(5-96_risq7rvr*-ac&=qa=(y97rd09*5u76d16'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'dj_rest_auth',
    'bearer_auth',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'dj_rest_auth.registration',
    'users',
    'accounts',
    'drf_yasg',
    'events',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'xaamga_api.urls'

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
        },
    },
]

WSGI_APPLICATION = 'xaamga_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# Configuration de la base de données sur LWS
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'cp1784679p21_xaamga_api',
#         'USER': 'cp1784679p21_xaamga',
#         'PASSWORD': 'Passer@123',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# } 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'xaamga_db',
        'USER': 'postgres',
        'PASSWORD': 'passer123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     #'rest_framework.permissions.IsAuthenticated',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

REST_AUTH_TOKEN_DEFAULTS = {
    'token_expires_in': 60,  # Token valid for 24 hours
}

AUTHENTICATION_BACKENDS = (
   "django.contrib.auth.backends.ModelBackend",
   "allauth.account.auth_backends.AuthenticationBackend",
#    "allauth.socialaccount.auth_backends.SocialAccountAuthBackend",
)


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "accounts.CustomUser"

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "fabricedjerabe01@gmail.com"
EMAIL_HOST_PASSWORD = "oneichtlpfssxwek"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'http://127.0.0.1:8000/api/v1/auth/login/'
LOGIN_URL = 'http://127.0.0.1:8000/api/v1/auth/login/'

REST_AUTH = {
    'PASSWORD_RESET_SERIALIZER': 'dj_rest_auth.serializers.PasswordResetSerializer',
    'PASSWORD_RESET_CONFIRM_SERIALIZER': 'dj_rest_auth.serializers.PasswordResetConfirmSerializer',
    'PASSWORD_CHANGE_SERIALIZER': 'dj_rest_auth.serializers.PasswordChangeSerializer',
    'OLD_PASSWORD_FIELD_ENABLED': True,
    # 'PASSWORD_RESET_USE_SITES_DOMAIN': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True,
}

EMAIL_CONFIRM_REDIRECT_BASE_URL = "http://localhost:3000/email/confirm/"

PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL = "http://localhost:8000/api/v1/auth/password/reset/confirm/"

# SESSION_COOKIE_SAMESITE = 'strict'
# SESSION_COOKIE_SECURE = True

SOCIALACCOUNT_PROVIDERS = { 
    'google' : { 
        'APP' : { 
            'client_id' : '343945259509-3t9jtv1g94m2a1poonintk3mdl56vrha.apps.googleusercontent.com' , 
            'secret' : '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' , 
            'key' : ''
         },
        ' SCOPE' : [ 
            'profil' , 
            'email' , 
        ], 
        'AUTH_PARAMS' : { 
            'access_type' : 'online' , 
        } 
    } 
}


SWAGGER_SETTINGS = {
    'LOGIN_URL': '/admin/login/',
    'LOGOUT_URL': '/admin/logout/',
}

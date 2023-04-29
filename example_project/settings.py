import os
from pathlib import Path

os.environ["PYTHONBREAKPOINT"] = "ipdb.set_trace"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_DIR = Path(__file__).resolve().parent
PARENT_DIR = PROJECT_DIR.parent
DEBUG = True

# Application definition
INSTALLED_APPS = [
    "adminlte3_admin",
    "adminlte3",
    "django.forms",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "example",
    "django_extensions",
    "debug_toolbar",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "adminlte3.context_processors.layout_settings",
                "adminlte3.context_processors.top_menu",
                "adminlte3.context_processors.user",
                # 'adminlte3.context_processors.sidebar_menu',
                "adminlte3_admin.context_processors.sidebar_menu",
                "adminlte3.context_processors.messages",
                "adminlte3.context_processors.notifications",
            ],
        },
    },
]

FORM_RENDERER = "adminlte3.renderers.DjangoTemplatesRenderer"


###
# Routes
# https://docs.djangoproject.com/en/3.2/howto/static-files/
######
ROOT_URLCONF = "urls"
WSGI_APPLICATION = "wsgi.application"
STATIC_URL = "/static/"


###
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
######
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": PROJECT_DIR / "db.sqlite3",
    }
}

# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

###
# Security
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
# https://docs.djangoproject.com/en/3.2/ref/contrib/auth/
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
######
SECRET_KEY = "changeme"
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
LOGIN_REDIRECT_URL = "/admin/"
LOGIN_URL = "/login/"
# LOGOUT_REDIRECT_URL="/"
# CSRF: https://www.django-rest-framework.org/topics/ajax-csrf-cors/#csrf-protection
# CORS: https://www.django-rest-framework.org/topics/ajax-csrf-cors/#cors

###
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
######
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
# LANGUAGES = [
#     ('pt_BR', _('Português do Brasil')),
#     ('en-us', _('English')),
# ]


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    "localhost",
    # ...
]

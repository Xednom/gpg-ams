import os
import logging
import environ

ROOT_DIR = environ.Path(__file__) - 2
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(DEBUG=(bool, False), )  # set default values and casting
env_file = str(ROOT_DIR.path('.env'))
env.read_env(env_file)

# Application definition

ADMIN_APPS = (
    'jet.dashboard',
    'jet',
)

LOCAL_APPS = (
    'admin_totals',
    'fillables',
    'users',
    'client',
    'reporting',
    'jobrequest',
    'carespecialist',
    'landmaster',
    'buyer',
    'seller',
    'logins',
    'accounts',
    'payroll',
    'reminders',
    'callmeinventory',
    'companyexpenses',
    'clienttimesheet',
    'inventory',
    'recruitment',
    'callmemasterboard'
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'rest_framework',
    'django_filters',
    'rest_framework_datatables',
    'corsheaders',
    'import_export',
    'crispy_forms',
    'notifications'
)

INSTALLED_APPS = ADMIN_APPS + DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

AUTH_USER_MODEL = 'users.CustomUser'
STAFFS = 'users.staffs'
CLIENTS = 'users.clients'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# To enable the sites framework
SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    '127.0.0.1:8000',
    'www.gpgcorp.com',
)

CORS_ALLOW_HEADERS = (
    'x-csrftoken'
)

# Django Jet Customization(s)
JET_CHANGE_FORM_SIBLING_LINKS = True
JET_SIDE_MENU_COMPACT = True
JET_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultIndexDashboard'
JET_APP_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultAppIndexDashboard'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework_datatables.filters.DatatablesFilterBackend',
    ),
}

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


# Logging
def levelname_filter(*args):
    class LevelNameFilter(logging.Filter):
        def filter(self, record):
            return record.levelname.lower() in args
    return LevelNameFilter


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
        'debug_only': {
            '()': levelname_filter('debug'),
        },
        'info_only': {
            '()': levelname_filter('info'),
        },
        'warn_only': {
            '()': levelname_filter('warning'),
        },
        'error_only': {
            '()': levelname_filter('error', 'critical'),
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'default': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'sitelog.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true', 'debug_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'debug.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'info': {
            'level': 'INFO',
            'filters': ['info_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'info.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'warning': {
            'level': 'WARNING',
            'filters': ['warn_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'warning.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'error.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['warning', 'error', 'default'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'default': {
            'handlers': ['console', 'default', 'debug', 'info'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'src'),
)

# for management command;
# see https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = (
    os.path.join(BASE_DIR, 'staticfiles')
)

MEDIA_URL = '/media/'
MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'media')
)
LOGIN_REDIRECT_URL = 'users:home'

LOGIN_URL = 'users:login'

LOGIN_EXEMPT_URLS = (
    'admin/',
    'users:login',
    'users:logout'
)

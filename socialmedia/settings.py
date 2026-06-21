from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-secret-key"

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'drf_spectacular',

    'accounts',
    'posts',
]


MIDDLEWARE = [

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


ROOT_URLCONF = 'socialmedia.urls'

TEMPLATES = [

    {

        'BACKEND':
        'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]


WSGI_APPLICATION='socialmedia.wsgi.application'


DATABASES={

'default':{

'ENGINE':'django.db.backends.sqlite3',

'NAME':BASE_DIR/'db.sqlite3',

}

}


LANGUAGE_CODE='en-us'

TIME_ZONE='Asia/Kolkata'

USE_TZ=True


STATIC_URL='static/'


MEDIA_URL='/media/'

MEDIA_ROOT=BASE_DIR/'media'


CORS_ALLOW_ALL_ORIGINS=True



REST_FRAMEWORK={


'DEFAULT_AUTHENTICATION_CLASSES':[

'rest_framework_simplejwt.authentication.JWTAuthentication'

],


'DEFAULT_PAGINATION_CLASS':

'rest_framework.pagination.PageNumberPagination',

'PAGE_SIZE':10,


'DEFAULT_SCHEMA_CLASS':

'drf_spectacular.openapi.AutoSchema'

}



SPECTACULAR_SETTINGS={

'TITLE':'Social Media API',

'VERSION':'1.0'

}
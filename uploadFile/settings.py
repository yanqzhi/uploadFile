"""
Django settings for uploadFile project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4@rb&la&))&k5!4qq+@gkl^sbuwcaza@r3h7%xi9z%f735pa#w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'uploadImage',
    'django.contrib.admin',
    'django.contrib.auth',
    # 'users',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels'
]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgi_redis.RedisChannelLayer',
        'CONFIG': {
#            'hosts': [('localhost', 6379)],
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
        'ROUTING': 'uploadFile.routing.channel_routing',
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'uploadFile.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'uploadFile.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME':  'uploadFile',
#         'USER':  'root',
#         'PASSWORD':  'Test13579',
#         'HOST': 'localhost',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


#AUTH_USER_MODEL = 'users.User'



LOGGING = {
    'version': 1,   # これを設定しないと怒られる
    'formatters': { # 出力フォーマットを文字列形式で指定する
        'all': {    # 出力フォーマットに`all`という名前をつける
            'format': '\t'.join([
                "[%(levelname)s]",
                "asctime:%(asctime)s",
                "module:%(module)s",
                "message:%(message)s",
                "process:%(process)d",
                "thread:%(thread)d",
            ])
        },
    },
    'handlers': {  # ログをどこに出すかの設定
        'file': {  # どこに出すかの設定に名前をつける `file`という名前をつけている
            'level': 'DEBUG',  # DEBUG以上のログを取り扱うという意味
            'class': 'logging.FileHandler',  # ログを出力するためのクラスを指定
            'filename': os.path.join(BASE_DIR, 'django.log'),  # どこに出すか
            'formatter': 'all',  # どの出力フォーマットで出すかを名前で指定
        },
        'console': { # どこに出すかの設定をもう一つ、こちらの設定には`console`という名前
            'level': 'DEBUG',
            # こちらは標準出力に出してくれるクラスを指定
            'class': 'logging.StreamHandler', 
            'formatter': 'all'
        },
    },
    'loggers': {  # どんなloggerがあるかを設定する
        'command': {  # commandという名前のloggerを定義
            'handlers': ['file', 'console'],  # 先述のfile, consoleの設定で出力
            'level': 'DEBUG',
        },
    },
}

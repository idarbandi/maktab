"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # بارگذاری متغیرهای محیطی از فایل .env

# مسیر اصلی پروژه را تعیین کنید
BASE_DIR = Path(__file__).resolve().parent.parent

# بارگذاری متغیرهای محیطی
DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')  # کلید مخفی پروژه
DEBUG = os.getenv('DEBUG', 'False') == 'True'  # حالت دیباگ
ALLOWED_HOSTS = []  # لیست هاست‌های مجاز

# تعریف برنامه‌های نصب شده
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'analytics',  # افزودن برنامه آنالیز
    "app",
    'profiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'corsheaders',  # پشتیبانی از CORS
    'django.contrib.sites',  # مطمئن شوید که این شامل شده است
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1  # شناسه سایت

# تعریف میان‌افزارها
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    'allauth.account.middleware.AccountMiddleware',  # برای احراز هویت
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'analytics.middleware.MaktabAnalyticsMiddleware',  # میان‌افزار برای آنالیز
    "analytics.middleware.MaktabAdminCheckMiddleware",  # میان‌افزار برای بررسی ادمین
]

# تنظیمات لاگینگ برای آنالیز
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'analytics.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# تنظیمات احراز هویت
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

CORS_ALLOW_ALL_ORIGINS = True  # برای مقاصد توسعه

# تنظیمات آدرس‌های ریشه‌ای
ROOT_URLCONF = "backend.urls"

# تنظیمات قالب‌ها
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
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"  # تنظیمات WSGI

# تنظیمات پایگاه داده
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# تنظیمات اعتبارسنجی رمز عبور
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

# تنظیمات بین‌المللی
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# تنظیمات فایل‌های استاتیک
STATIC_URL = "static/"

# تنظیمات نوع کلید اصلی پیش‌فرض
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# تنظیمات REST framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'rest_framework.authentication.TokenAuthentication',
        "rest_framework.authentication.SessionAuthentication"
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        'rest_framework.permissions.IsAuthenticated',
    ],
    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,  # اندازه صفحه‌بندی سفارشی
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ]
}

# تنظیمات حساب‌ها
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGIN_METHODS = {'email'}

# تنظیمات ارائه دهندگان اجتماعی
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
        'REDIRECT_URI': 'http://127.0.0.1:8000/accounts/google/login/callback/'
    }
}

# URL ها برای تأیید ایمیل
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'http://127.0.0.1:8080/login'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'http://127.0.0.1:8080/register'

# تنظیمات ایمیل
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# تنظیمات CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

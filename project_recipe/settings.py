"""
Налаштування Django для проєкту project_recipe.

Згенеровано за допомогою 'django-admin startproject' (Django 4.2.1).
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Завантаження змінних середовища з файлу .env
load_dotenv()

# Базовий шлях до директорії проєкту
BASE_DIR = Path(__file__).resolve().parent.parent

# ПОПЕРЕДЖЕННЯ БЕЗПЕКИ: зберігайте секретний ключ у таємниці!
# Беремо значення з .env. Якщо його там немає, викидаємо помилку або використовуємо дефолтне
SECRET_KEY = os.environ.get('SECRET_KEY')

# ПОПЕРЕДЖЕННЯ БЕЗПЕКИ: не запускайте з увімкненим debug у продакшені!
DEBUG = os.environ.get('DEBUG') == 'True'

ALLOWED_HOSTS = []

# Визначення аплікацій
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'recipe.apps.RecipeConfig',
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

ROOT_URLCONF = 'project_recipe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'project_recipe.wsgi.application'

# База даних
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валідація паролів
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

# Інтернаціоналізація
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статичні файли (CSS, JavaScript, зображення)
STATIC_URL = 'static/'

# Тип первинного ключа за замовчуванням
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
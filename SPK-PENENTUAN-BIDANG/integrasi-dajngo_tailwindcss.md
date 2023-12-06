# Instalation
- create project : django-admin startproject myproject
- masuk ke project : cd myproject
- install tailwind : pip install tailwind
    - daftarkan ke INSTALLED_APPS :
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            <!-- TAILWINDCSS -->
            'tailwind',
            'APP',
        ]

    - pip install django-tailwind
    - python manage.py tailwind init
        theme
    - daftarkan ke INSTALLED_APPS :
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            <!-- TAILWINDCSS -->
            'tailwind',
            'theme',
            'APP',
        ]
    - taruh TAILWIND_APP_NAME = 'theme' di bawah INSTALLED_APPS
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            <!-- TAILWINDCSS -->
            'tailwind',
            'theme',
            'APP',
        ]
        <!-- tambahkan -->
        TAILWIND_APP_NAME = 'theme'

        INTERNAL_IPS = [
            "127.0.0.1",
        ]

        NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"


- python manage.py tailwind install
    - masukan NPM_BIN_PATH = "/usr/local/bin/npm"
    - buka cmd dan ketikan : where npm
    - copas dan ganti sesui alamat NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
    - jalankan kembali : python manage.py tailwind install
    
- komfigurasi file static
- python manage.py collectstatic
- kofigurasi templates
- buat app
- jalankan tailwind : python manage.py tailwind star
- testing pada templates
 {% load static tailwind_tags %}
- taruh teg ini di dalam head
 {% tailwind_css %}


    


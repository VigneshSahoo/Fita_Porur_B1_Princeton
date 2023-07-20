pip install django
django-admin # Just for verification
django-admin startproject fita .
python manage.py runserver 80 # to start the webserver

Open a new terminal and check for manage.py

django-admin startapp home
python manage.py migrate

pip install mysqlclient
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fita',
        'USER': 'root',
        'PASSWORD': 'Fita@1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

{% include 'nav.html' %}
{% extends 'base.html' %}
{{
    Dynamic variable
}}

django-admin startproject website_17_july .
python manage.py runserver 80

Models    - Data
Views     - static 
Templates - html

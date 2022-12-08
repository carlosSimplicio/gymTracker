#!/bin/ash

export DJANGO_SUPERUSER_EMAIL=admin@admin.com
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin

# Hackzinho pra esperar o db subir
sleep 10


./manage.py migrate
./manage.py createsuperuser --noinput
./manage.py runserver 0.0.0.0:8000
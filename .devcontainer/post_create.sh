export DJANGO_SUPERUSER_EMAIL=admin@admin.com
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin

cd backend

./manage.py migrate
./manage.py createsuperuser --noinput

cd ../frontend

npm install

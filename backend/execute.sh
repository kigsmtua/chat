python manage.py makemigrations --noinput --settings=$DJANGO_SETTINGS_MODULE
python manage.py migrate --noinput --settings=$DJANGO_SETTINGS_MODULE
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000 --settings=$DJANGO_SETTINGS_MODULE

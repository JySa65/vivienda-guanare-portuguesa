# Proyecto Vivienda

## Requirements
* Git
* Python 3
* Virtualenv

## Install

1. Create VirtualEnv

        python3 -m virtualenv .env

1. Activate VirtualEnv

        source .env/bin/activate

1. Install Requirements.txt

        pip install -r requirements.txt

## Run Project dev

        (.env) ➜  python manage.py migrate
        (.env) ➜  python manage.py createsuperuser
        (.env) ➜  python manage.py runserver --settings=vivienda.local_settings

## Run Project prod

        (.env) ➜  python manage.py migrate
        (.env) ➜  python manage.py createsuperuser
        (.env) ➜  python manage.py collectstatic
        (.env) ➜  gunicorn vivienda.wsgi   

## App Page

1. Access to page [localhost:8000/](http://localhost:8000/)

1. Access Server Page [https://vivienda-2018-guanare.herokuapp.com/](https://vivienda-2018-guanare.herokuapp.com/)

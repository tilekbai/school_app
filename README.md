# school_app
Здравствуйте. Это приложение является автоматизацией некоторых школьных процессов. 

### Установка
`$git clone --branch master <githubrepo>`

После клонирования проекта Вам нужно создать .env файл с данными для базы данных и остальных настроек. 
В этом файле вам нужно перечислить следующие данные:

DEBUG={your_value}

SECRET_KEY={your secret key}

NAME={your db_name}

USER={your db_user}

PASSWORD={your db_user_password}

HOST={your db_host}

PORT={your db_port}

EMAIL_HOST_USER = {your email host user}

EMAIL_HOST_PASSWORD = {your email host password}

### Запуск

`$ docker-compose build `

`$ docker-compose run web python manage.py migrate`

`$ docker-compose up`

### Примечания:

Если вы пользуетесь compose версией 2.0 и выше, то используйте `docker compose` (без -)

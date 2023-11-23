# Run with Docker-compose
## Building a Docker Image:
```shell
docker-compose build
```

## Applying Migrations:
```shell
docker-compose exec app python manage.py migrate
```

## Running containers/reload building:
```shell
docker-compose up --build
```

# Run without Docker-compose 
### Installation and configuration
#### Install dependencies

```shell
pip install -r requirements.txt
```
### Example .env

```shell
SECRET_KEY=

POSTGRES_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
POSTGRES_HOST=
POSTGRES_PORT=

PUBLISHABLE_KEY_STRIPE=
SECRET_KEY_STRIPE=
```
#### Apply migrations

```shell
python3 manage.py migrate
```

### Populate the database

```shell
python manage.py put_data
python manage.py createsuperuser
```

### Run the Server

```shell
python3 manage.py runserver
```

### Django + Stripe API бэкенд со следующим функционалом и условиями:

- создана модель Item с полями (name, description, price); 
- API с двумя методами:
    GET /buy/{id}, c помощью которого можно получить Stripe Intent Id для оплаты выбранного Item. 
    GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном 
        Item и кнопка Buy. По нажатию на кнопки Buy  происходит запрос на /buy/{id}, получение intent_id и 
        далее необходимо подтвердить платежное намерение с помощью тестовой карты:

```shell
4242424242424242 12 34 567 12345
```

- Запуск используя Docker;
- Использование environment variables;
- Просмотр Django Моделей в Django Admin панели;
- Реализовал не Stripe Session, а Stripe Payment Intent.

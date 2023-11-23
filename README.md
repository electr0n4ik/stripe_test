# Запуск с помощью docker-compose
## Сборка докер-образов:
```shell
sudo docker-compose build
```

## Запуск контейнеров:
```shell
sudo docker-compose up --build
```

## Применение миграций и наполнение БД в запущенном докере:
```shell
sudo docker-compose exec app python manage.py migrate
sudo docker-compose exec app python manage.py put_data
sudo docker-compose exec app python manage.py createsuperuser
```

# Запуск без докера

### Устанавка пакетов 

```shell
pip install -r requirements.txt
```
### Пример файла .env

```shell
SECRET_KEY=

POSTGRES_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_PORT=


PUBLISHABLE_KEY_STRIPE=
SECRET_KEY_STRIPE=
```
#### Применение миграций

```shell
python3 manage.py migrate
```

### Наполнение БД

```shell
python manage.py put_data
python manage.py createsuperuser
```

### Запуск сервера

```shell
python3 manage.py runserver
```

### Django + Stripe API бэкенд со следующим функционалом и условиями:

- создана модель Item с полями (name, description, price); 
- API с двумя методами:

    GET /buy/{id}, можно получить Stripe Intent Id для оплаты выбранного Item. 
    
    GET /item/{id}, можно получить простейшую HTML страницу, на которой будет информация о выбранном 
    Item и кнопка Buy. По нажатию на кнопки Buy происходит запрос на /buy/{id}, получение intent_id и 
    далее необходимо подтвердить платежное намерение с помощью тестовой карты:

```
4242424242424242 12 34 567 12345
```

- Запуск используя Docker;
- Использование environment variables;
- Просмотр Django Моделей в Django Admin панели;
- Реализовал не Stripe Session, а Stripe Payment Intent.

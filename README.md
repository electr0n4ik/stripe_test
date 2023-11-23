Django + Stripe API бэкенд со следующим функционалом и условиями:

Django Модель Item с полями (name, description, price) 
- API с двумя методами:
    GET /buy/{id}, c помощью которого можно получить Stripe Intent Id для оплаты выбранного Item. 
    GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном 
        Item и кнопка Buy. По нажатию на кнопки Buy  происходит запрос на /buy/{id}, получение intent_id и 
        далее происходит переход на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

- Использование environment variables;
- Просмотр Django Моделей в Django Admin панели
- Реализовал не Stripe Session, а Stripe Payment Intent.


### put_data

Add 3 products to the database

```shell
python manage.py put_data
```

python manage.py createsuperuser


### Example .env

```shell
SECRET_KEY=

POSTGRES_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=

PUBLISHABLE_KEY_STRIPE=
SECRET_KEY_STRIPE=
```
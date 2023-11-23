import json
import os

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
import stripe

from config.settings import SECRET_KEY_STRIPE
from .models import Item

stripe.api_key = SECRET_KEY_STRIPE


class BuyItemView(View):
    def get(self, request, *args, **kwargs):

        item = get_object_or_404(Item, id=kwargs['id'])
        amount = int(item.price) * 100
        currency = 'usd'
        description = str(item.description)
        statement_descriptor = 'OKPay'

        stripe.api_key = settings.SECRET_KEY_STRIPE

        # Платежный интент
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=['card'],
            description=description,
            statement_descriptor=statement_descriptor,
        )

        # client_secret из интента
        return JsonResponse({'client_secret': intent.client_secret})


class ItemDetailView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)

        context = {'item': item,
                   'stripe_public_key': stripe.api_key}
        return render(request, 'item_detail.html', context)

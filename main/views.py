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

        intent = stripe.PaymentIntent.create(
            amount=int(item.price) * 100,
            currency='usd',
            payment_method_types=['card'],
            description=str(item.description),
            statement_descriptor='OKPay',
        )

        context = {'client_secret': intent.client_secret,
                   'intentId': intent.id,
                   'public_key': settings.PUBLISHABLE_KEY_STRIPE}

        return render(request, 'checkout_page.html', context)
        # return JsonResponse(context)


class ItemDetailView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)

        context = {'item': item,
                   'stripe_public_key': settings.PUBLISHABLE_KEY_STRIPE}
        return render(request, 'item_detail.html', context)

import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
import stripe
from .models import Item

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


class BuyItemView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)

        # Создание Stripe Session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'name': item.name,
                'description': item.description,
                'amount': int(item.price * 100),  # в центах
                'currency': 'usd',
                'quantity': 1,
            }],
            success_url=request.build_absolute_uri(item.get_absolute_url()),
            cancel_url=request.build_absolute_uri(item.get_absolute_url()),
        )

        return JsonResponse({'session_id': session.id})


class ItemDetailView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)

        context = {'item': item}
        return render(request, 'item_detail.html', context)

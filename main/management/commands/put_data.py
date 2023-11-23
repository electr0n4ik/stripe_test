from django.core.management import BaseCommand

from main.models import Item


class Command(BaseCommand):

    def handle(self, *args, **options):
        item_list = [
            {"name": "Test1", "description": "Testing item1 to stripe",
             "price": 100},
            {"name": "Test2", "description": "Testing item2 to stripe",
             "price": 200},
            {"name": "Test3", "description": "Testing item3 to stripe",
             "price": 300},

        ]
        for element in item_list:
            Item.objects.get_or_create(**element)

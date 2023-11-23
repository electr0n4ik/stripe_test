from django.db import models
from django.urls import reverse


NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):

    name = models.CharField(
        max_length=127,
        verbose_name='название')
    description = models.TextField(
        max_length=255,
        **NULLABLE,
        verbose_name='описание')
    price = models.IntegerField(verbose_name="цена, $")

    def __str__(self):
        return f"Товар {self.name}"

    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

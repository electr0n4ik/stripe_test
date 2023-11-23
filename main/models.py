from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):

    name = models.CharField(
        max_length=127,
        verbose_name='название')
    description = models.TextField(
        max_length=255,
        **NULLABLE,
        verbose_name='описание')
    price = models.IntegerField(verbose_name="цена")

    def __str__(self):
        return f"Товар {self.name}"

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

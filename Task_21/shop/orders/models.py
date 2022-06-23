from django.db import models
from django.contrib.auth.models import User

from clothing_store.models import Item


class Order(models.Model):
    items = models.ManyToManyField(Item, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')

    class Meta:
        verbose_name_plural = 'Заказ'

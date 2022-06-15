from django.db import models
from clothing_store.models import Clothing
from django.contrib.auth.models import User


class Order(models.Model):
    clothing = models.ManyToManyField(Clothing, related_name='orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')

    class Meta:
        verbose_name_plural = 'Заказ'

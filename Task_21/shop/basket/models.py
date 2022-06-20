from django.db import models
from django.contrib.auth.models import User
from clothing_store.models import Clothing


class Cart(models.Model):
    clothing = models.ManyToManyField(Clothing, related_name='carts')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'Cart for {self.user}'

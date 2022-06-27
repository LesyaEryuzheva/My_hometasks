from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Бренд'

    def __str__(self):
        return self.name


class Clothing(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Одежда'

    def __str__(self):
        return self.name


class Item(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    clothing = models.ForeignKey('Clothing', on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Вещь'

    def __str__(self):
        return f'{self.name}, {self.price}$, {self.brand}'

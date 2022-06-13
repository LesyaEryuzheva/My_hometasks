from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.country}'


class CarModel(models.Model):
    name_model = models.CharField(max_length=20)
    car_body = models.CharField(max_length=20, blank=True)
    brand = models.ForeignKey(Brand, models.PROTECT, null=True)

    def __str__(self):
        return f'{self.name_model} {self.car_body}'


class Engine(models.Model):
    type = models.CharField(max_length=20)
    volume = models.FloatField()
    car_model = models.ManyToManyField(CarModel, related_name='engines')

    def __str__(self):
        return f'{self.type} {self.volume}'

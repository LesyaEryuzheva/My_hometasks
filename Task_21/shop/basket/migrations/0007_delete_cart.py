# Generated by Django 4.0.5 on 2022-06-13 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0006_remove_cart_product_price_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]

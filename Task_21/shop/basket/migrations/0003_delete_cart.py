# Generated by Django 4.0.5 on 2022-06-13 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_alter_cart_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing_store', '0006_alter_brand_name_alter_clothing_name'),
        ('orders', '0002_remove_order_clothing_order_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(related_name='orders', to='clothing_store.item'),
        ),
    ]

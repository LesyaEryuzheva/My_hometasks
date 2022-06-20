# Generated by Django 4.0 on 2022-06-20 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing_store', '0004_remove_clothing_image'),
        ('basket', '0014_remove_cart_clothes_quantity_remove_cart_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='clothes',
        ),
        migrations.AddField(
            model_name='cart',
            name='clothing',
            field=models.ManyToManyField(related_name='clothing', to='clothing_store.Clothing'),
        ),
    ]

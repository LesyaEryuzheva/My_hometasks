# Generated by Django 4.0.5 on 2022-06-20 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothing_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name_plural': 'Вещь'},
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='description',
        ),
    ]

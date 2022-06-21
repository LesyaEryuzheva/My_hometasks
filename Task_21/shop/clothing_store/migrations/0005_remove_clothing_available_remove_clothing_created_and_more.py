# Generated by Django 4.0 on 2022-06-20 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('clothing_store', '0004_remove_clothing_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothing',
            name='available',
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='created',
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='price',
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='user',
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('clothing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='clothing_store.clothing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Пользователь')),
            ],
        ),
    ]

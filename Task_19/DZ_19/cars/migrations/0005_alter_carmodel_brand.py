# Generated by Django 4.0.4 on 2022-06-05 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_remove_brand_id_alter_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cars.brand'),
        ),
    ]

# Generated by Django 3.2.15 on 2023-04-09 11:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0047_rename_restaurant_order_assigned_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='quantity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='количество'),
        ),
    ]

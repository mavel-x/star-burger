# Generated by Django 3.2.15 on 2023-04-09 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0046_auto_20230312_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='restaurant',
            new_name='assigned_restaurant',
        ),
    ]

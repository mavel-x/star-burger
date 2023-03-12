# Generated by Django 3.2.15 on 2023-03-12 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0045_auto_20230311_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='foodcartapp.restaurant', verbose_name='ответственный ресторан'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, choices=[(None, ''), ('CASH', 'Наличные'), ('CARD', 'Карта')], db_index=True, max_length=4, null=True, verbose_name='способ оплаты'),
        ),
    ]

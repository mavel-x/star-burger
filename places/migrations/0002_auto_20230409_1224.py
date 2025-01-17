# Generated by Django 3.2.15 on 2023-04-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='широта'),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='долгота'),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='out_of_stock',
            field=models.BooleanField(default=False, verbose_name='Нет в наличии'),
        ),
    ]

# Generated by Django 3.1.4 on 2021-01-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BAYI', '0003_customersorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersorders',
            name='priceSold',
            field=models.FloatField(default=0, verbose_name='Satış Fiyatı'),
        ),
    ]
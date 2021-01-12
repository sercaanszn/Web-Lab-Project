# Generated by Django 3.1.4 on 2021-01-01 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSB', '0002_auto_20210101_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materialName', models.CharField(max_length=100)),
                ('materialUnit', models.CharField(max_length=100)),
                ('materialStockCount', models.IntegerField(default=0)),
                ('estimatedSupply', models.IntegerField(default=0)),
                ('tresholdValue', models.IntegerField(default=0)),
                ('unitPrice', models.IntegerField(default=0)),
                ('lastOrder', models.DateField()),
            ],
        ),
    ]

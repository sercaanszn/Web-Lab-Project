# Generated by Django 3.1.5 on 2021-01-16 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SSB', '0018_auto_20210116_2105'),
        ('BAYI', '0006_auto_20210116_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customersorders',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SSB.products', verbose_name='Ürün'),
        ),
    ]
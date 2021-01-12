# Generated by Django 3.1.4 on 2021-01-09 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SSB', '0012_auto_20210109_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='productStock',
            field=models.IntegerField(default=0, verbose_name='Stok Adedi'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='estimatedSupply',
            field=models.IntegerField(default=0, verbose_name='Tahmini Temin Süresi'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='lastOrder',
            field=models.DateField(verbose_name='Son Sipariş'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='materialName',
            field=models.CharField(max_length=100, verbose_name='Hammadde Adı'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='materialStockCount',
            field=models.FloatField(default=0, verbose_name='Stok Miktarı'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='materialUnit',
            field=models.CharField(max_length=100, verbose_name='Birim'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='tresholdValue',
            field=models.FloatField(default=0, verbose_name='Eşik Değer'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='unitPrice',
            field=models.FloatField(default=0, verbose_name='Birim Fiyat'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderedProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_blogs', to='SSB.products', verbose_name='Ürün'),
        ),
    ]

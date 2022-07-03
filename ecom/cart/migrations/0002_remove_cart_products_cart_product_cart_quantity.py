# Generated by Django 4.0.5 on 2022-07-03 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220626_1243'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Products',
        ),
        migrations.AddField(
            model_name='cart',
            name='Product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='Quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

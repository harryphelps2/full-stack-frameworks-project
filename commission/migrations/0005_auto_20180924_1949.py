# Generated by Django 2.1.1 on 2018-09-24 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0004_auto_20180924_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null='True'),
        ),
    ]
# Generated by Django 2.1.1 on 2018-09-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_auto_20180922_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='original',
            name='highest_bid',
            field=models.IntegerField(),
        ),
    ]
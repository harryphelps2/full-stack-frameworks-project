# Generated by Django 2.1.1 on 2018-09-18 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_original_highest_bidder'),
    ]

    operations = [
        migrations.AddField(
            model_name='original',
            name='paid',
            field=models.BooleanField(null='True'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='original',
            name='end_date',
            field=models.DateField(null='True'),
        ),
        migrations.AlterField(
            model_name='original',
            name='start_date',
            field=models.DateField(null='True'),
        ),
    ]

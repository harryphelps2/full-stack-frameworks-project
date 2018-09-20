# Generated by Django 2.1.1 on 2018-09-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auto_20180918_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='original',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='original',
            name='start_date',
        ),
        migrations.AddField(
            model_name='original',
            name='bid_time',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='original',
            name='end_date_time',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='original',
            name='start_date_time',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
    ]

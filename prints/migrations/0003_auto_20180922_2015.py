# Generated by Django 2.1.1 on 2018-09-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prints', '0002_auto_20180909_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='print',
            name='price',
            field=models.IntegerField(),
        ),
    ]

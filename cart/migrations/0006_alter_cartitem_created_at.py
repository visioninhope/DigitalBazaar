# Generated by Django 4.1.1 on 2022-10-05 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_cartitem_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 10, 5, 14, 15, 22, 326739)),
        ),
    ]
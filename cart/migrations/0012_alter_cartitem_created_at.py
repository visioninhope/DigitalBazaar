# Generated by Django 4.1.5 on 2023-09-27 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_cartitem_status_alter_cartitem_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 9, 27, 13, 27, 24, 712080)),
        ),
    ]
# Generated by Django 4.1.5 on 2023-05-12 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 5, 12, 21, 15, 31, 579174)),
        ),
    ]
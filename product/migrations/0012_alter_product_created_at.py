# Generated by Django 4.1.5 on 2023-05-13 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 5, 13, 13, 48, 10, 25294)),
        ),
    ]
# Generated by Django 3.0.6 on 2020-10-12 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_john', '0002_auto_20201002_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 12, 16, 1, 6, 810656)),
        ),
    ]

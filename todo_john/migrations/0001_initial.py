# Generated by Django 3.0.6 on 2020-09-30 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('time', models.DateTimeField(default=datetime.datetime(2020, 9, 30, 12, 46, 12, 177044))),
            ],
        ),
    ]
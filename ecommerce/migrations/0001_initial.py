# Generated by Django 3.0.6 on 2020-10-12 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecommerce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='pics')),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 10, 12, 16, 1, 6, 813656))),
            ],
        ),
    ]

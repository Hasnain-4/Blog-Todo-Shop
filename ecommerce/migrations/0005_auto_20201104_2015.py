# Generated by Django 3.0.6 on 2020-11-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_productdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Electronics_ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ortitle1', models.CharField(max_length=255)),
                ('ordesc1', models.TextField()),
                ('orimg1', models.ImageField(upload_to='ordered_products')),
                ('orqnty1', models.IntegerField()),
                ('oraddress1', models.CharField(max_length=255)),
                ('orpin1', models.IntegerField()),
                ('ordist1', models.CharField(max_length=255)),
                ('orcntry1', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Utencils_ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ortitle2', models.CharField(max_length=255)),
                ('ordesc2', models.TextField()),
                ('orimg2', models.ImageField(upload_to='ordered_products')),
                ('orqnty2', models.IntegerField()),
                ('oraddress2', models.CharField(max_length=255)),
                ('orpin2', models.IntegerField()),
                ('ordist2', models.CharField(max_length=255)),
                ('orcntry2', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='ProductDetail',
            new_name='Clothes_ProductDetail',
        ),
    ]

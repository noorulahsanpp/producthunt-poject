# Generated by Django 3.0.4 on 2020-03-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200330_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

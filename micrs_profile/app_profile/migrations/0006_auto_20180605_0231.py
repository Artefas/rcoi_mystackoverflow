# Generated by Django 2.0.6 on 2018-06-04 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0005_auto_20180605_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.CharField(default=None, max_length=256, null=True),
        ),
    ]

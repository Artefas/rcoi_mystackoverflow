# Generated by Django 2.0.6 on 2018-06-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0004_auto_20180605_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='url_facebook',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='url_github',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='url_twitter',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='url_vk',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
    ]

# Generated by Django 3.2.1 on 2021-05-06 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_user_device_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='device_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

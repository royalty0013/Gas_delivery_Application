# Generated by Django 3.1.7 on 2021-05-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0011_auto_20210501_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_details',
            name='card_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

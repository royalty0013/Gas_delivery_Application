# Generated by Django 3.1.7 on 2021-04-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_auto_20210430_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_details',
            name='card_number',
            field=models.BigIntegerField(),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-30 12:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_auto_20210430_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportation_cost_per_km',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transportation_cost_per_km',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

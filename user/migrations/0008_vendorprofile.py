# Generated by Django 3.1.7 on 2021-04-21 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210419_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('user_type', models.CharField(choices=[('Customer', 'Customer'), ('Vendor', 'Vendor'), ('Transporter', 'Transporter')], default='Vendor', max_length=20)),
                ('address', models.TextField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

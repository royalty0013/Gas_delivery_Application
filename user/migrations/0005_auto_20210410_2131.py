# Generated by Django 3.1.7 on 2021-04-10 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210406_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_purchased', models.JSONField()),
                ('price', models.FloatField()),
                ('vendor_completed', models.BooleanField(default=False)),
                ('transporter_completed', models.BooleanField(default=False)),
                ('customer_completed', models.BooleanField(default=False)),
                ('total_price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Purchase Records',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Customer', 'Customer'), ('Vendor', 'Vendor'), ('Transporter', 'Transporter')], default='Customer', max_length=20),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_completed', models.BooleanField(default=False)),
                ('transaction_verified', models.BooleanField(default=False)),
                ('Reference_id', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer_name', to=settings.AUTH_USER_MODEL)),
                ('purchase_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Customer_purchase', to='user.purchase')),
                ('transporter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_guy', to=settings.AUTH_USER_MODEL)),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vendor_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Transaction Records',
            },
        ),
        migrations.AddField(
            model_name='purchase',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer_account', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchase',
            name='vendor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vendor', to=settings.AUTH_USER_MODEL),
        ),
    ]

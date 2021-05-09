# Generated by Django 3.2.1 on 2021-05-09 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_remove_vendor_shop_user_type'),
        ('transaction', '0019_auto_20210509_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='vendor_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Vendor_name', to='user.vendor_shop'),
        ),
    ]

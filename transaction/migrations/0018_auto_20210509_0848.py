# Generated by Django 3.2.1 on 2021-05-09 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0014_remove_vendor_shop_user_type'),
        ('transaction', '0017_purchase_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='vendor_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Vendor_name', to='user.vendor_shop'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='vendor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Vendor', to=settings.AUTH_USER_MODEL),
        ),
    ]

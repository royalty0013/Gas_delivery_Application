from django.db import models
import jsonfield
from django.utils import timezone
from user.models import User
from user.models import Vendor_shop

# Create your models here.

class Purchase(models.Model):
    customer_id = models.ForeignKey(User, related_name="Customer_account", on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(Vendor_shop, related_name="Vendor", on_delete=models.CASCADE)
    items_purchased = models.JSONField()
    item_cost = models.FloatField(default=0)
    transporter = models.CharField(max_length=50, null=True)
    transportation_cost = models.FloatField(default=0)
    transaction_completed = models.BooleanField(default=False)
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Purchase Records"

class Transportation_cost_per_km(models.Model):
    unit_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Delivery Unit price/Km"


class Transaction(models.Model):
    customer_id = models.ForeignKey(User, related_name="Customer_name", on_delete=models.CASCADE)
    transporter_id = models.ForeignKey(User, related_name="delivery_guy", on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(User, related_name="Vendor_name", on_delete=models.CASCADE)
    transaction_completed = models.BooleanField(default=False)
    transaction_verified = models.BooleanField(default=False)
    Reference_id = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Transaction Records"

class Gas_Sizes(models.Model):
    title = models.CharField(max_length=50, null=True)
    price = models.FloatField()
    litre_number = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at =models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Gas Sizes"

class Card_details(models.Model):
    user = models.ForeignKey(User, related_name="customer_card_detail", on_delete=models.CASCADE, null=True)
    card_type = models.CharField(max_length=30, null=True)
    card_number = models.CharField(max_length=25, null=True)
    CVV = models.IntegerField()
    expiry_date = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Customer Card Details"

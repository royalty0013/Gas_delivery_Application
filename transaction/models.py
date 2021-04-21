from django.db import models
import jsonfield
from django.utils import timezone
from user.models import User

# Create your models here.

class Purchase(models.Model):
    customer_id = models.ForeignKey(User, related_name="Customer_account", on_delete=models.CASCADE)
    items_purchased = models.JSONField()
    price = models.FloatField()
    vendor_id = models.ForeignKey(User, related_name="Vendor", on_delete=models.CASCADE) 
    vendor_completed = models.BooleanField(default=False)
    transporter_completed = models.BooleanField(default=False)
    customer_completed = models.BooleanField(default=False)
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Purchase Records"

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

from django.contrib import admin
from .models import Purchase, Transaction
# Register your models here.

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'items_purchased', 'price','vendor_id', 'vendor_completed','transporter_completed', 'customer_completed', 'total_price', 'created_at', 'updated_at']
admin.site.register(Purchase, PurchaseAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = [ 'customer_id', 'transporter_id','vendor_id', 'transaction_completed','transaction_verified', 'Reference_id',  'created_at', 'updated_at']
admin.site.register(Transaction, TransactionAdmin)
from django.contrib import admin
from user.models import User, Purchase, Transaction

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'user_type', 'is_verified','is_staff', 'is_superuser', 'is_active', 'created_at', 'updated_at']
admin.site.register(User, UserAdmin)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'items_purchased', 'price','vendor_id', 'vendor_completed','transporter_completed', 'customer_completed', 'total_price', 'created_at', 'updated_at']
admin.site.register(Purchase, PurchaseAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = [ 'customer_id', 'transporter_id','vendor_id', 'transaction_completed','transaction_verified', 'Reference_id',  'created_at', 'updated_at']
admin.site.register(Transaction, TransactionAdmin)
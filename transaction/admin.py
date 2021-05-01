from django.contrib import admin
from .models import Purchase, Transaction, Gas_Sizes, Transportation_cost_per_km, Card_details
# Register your models here.

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'vendor_id', 'items_purchased', 'item_cost', 'transporter', 'transportation_cost', 'vendor_completed','transporter_completed', 'customer_completed', 'total_price', 'created_at', 'updated_at']
admin.site.register(Purchase, PurchaseAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = [ 'customer_id', 'transporter_id','vendor_id', 'transaction_completed','transaction_verified', 'Reference_id',  'created_at', 'updated_at']
admin.site.register(Transaction, TransactionAdmin)

class Gas_SizesAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'price','litre_number','created_at', 'updated_at']
admin.site.register(Gas_Sizes, Gas_SizesAdmin)

class TransporterUnitPriceAdmin(admin.ModelAdmin):
    list_display = ['unit_price','created_at', 'updated_at']
admin.site.register(Transportation_cost_per_km, TransporterUnitPriceAdmin)

class Card_detailsAdmin(admin.ModelAdmin):
    list_display = ['user','card_type', 'card_number', 'CVV', 'expiry_date', 'created_at', 'updated_at']
admin.site.register(Card_details, Card_detailsAdmin)

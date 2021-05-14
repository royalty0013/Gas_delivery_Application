from django.contrib import admin
from .models import Purchase, Transaction, Gas_Sizes, Transportation_cost_per_km, Card_details
# Register your models here.

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer','closest_vendor', 'accepted_vendor', 'vendor_name','items_purchased', 'item_cost', 'transporter', 'transporter_name', 'distance', 'transportation_cost', 'transaction_completed', 'total_price', 'created_at', 'updated_at']
admin.site.register(Purchase, PurchaseAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = [ 'customer', 'transporter','vendor', 'transaction_completed','transaction_verified', 'reference',  'created_at', 'updated_at']
admin.site.register(Transaction, TransactionAdmin)

class Gas_SizesAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'price','litre_number','created_at', 'updated_at']
admin.site.register(Gas_Sizes, Gas_SizesAdmin)

class TransporterUnitPriceAdmin(admin.ModelAdmin):
    list_display = ['unit_price','created_at', 'updated_at']
admin.site.register(Transportation_cost_per_km, TransporterUnitPriceAdmin)

class Card_detailsAdmin(admin.ModelAdmin):
    list_display = ['user','card_type', 'card_number', 'cvv', 'expiry_date', 'created_at', 'updated_at']
admin.site.register(Card_details, Card_detailsAdmin)

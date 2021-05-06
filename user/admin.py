from django.contrib import admin
from user.models import User, Vendor_shop
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'user_type', 'device_token', 'is_verified','is_staff', 'is_superuser', 'is_active', 'created_at', 'updated_at']
admin.site.register(User, UserAdmin)

class Vendor_shopAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'company_name', 'user_type','phone_number', 'address', 'longitude','latitude','created_at', 'updated_at']
admin.site.register(Vendor_shop, Vendor_shopAdmin)


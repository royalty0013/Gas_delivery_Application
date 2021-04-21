from django.contrib import admin
from user.models import User, VendorProfile
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'user_type', 'is_verified','is_staff', 'is_superuser', 'is_active', 'created_at', 'updated_at']
admin.site.register(User, UserAdmin)

class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'company_name', 'user_type', 'address', 'longitude','latitude','created_at', 'updated_at']
admin.site.register(VendorProfile, VendorProfileAdmin)


from django.contrib import admin
from user.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'user_type', 'is_verified','is_staff', 'is_superuser', 'is_active', 'created_at', 'updated_at']
admin.site.register(User, UserAdmin)


from django.contrib import admin
from gateway.models import Jwt
# Register your models here.

class JwtAdmin(admin.ModelAdmin):
    list_display = ['user', 'access', 'refresh', 'created_at', 'updated_at']
admin.site.register(Jwt, JwtAdmin)
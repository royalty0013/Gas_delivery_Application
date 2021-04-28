from rest_framework import serializers
from .models import Vendor_shop

class Vendor_shopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor_shop
        fields = ["latitude", "longitude"]
        latitude = serializers.FloatField()
        longitude = serializers.FloatField()
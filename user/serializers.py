from rest_framework import serializers
from .models import Vendor_shop, User

class Vendor_shop_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor_shop
        fields = ["latitude", "longitude"]
        latitude = serializers.FloatField()
        longitude = serializers.FloatField()

class Update_Device_Token_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["device_token"]

    def update(self, instance, validated_data):
        instance.device_token = validated_data.get('device_token', instance.device_token)
        instance.save()
        return instance
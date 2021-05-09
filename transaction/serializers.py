from rest_framework import serializers
from .models import Transaction, Gas_Sizes, Card_details, Purchase
from user.models import User

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

class Gas_SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gas_Sizes
        fields = "__all__"

class Card_detailsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    class Meta:
        model = Card_details
        fields = "__all__"

class TransactionStatusSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()

    def get_customer_name(self, obj):
        return obj.customer.name
    class Meta:
        model = Purchase
        fields = "__all__"
        # read_only_fields = ["customer_name"]

class PurchaseSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source="user.email")
    class Meta:
        model = Purchase
        fields = "__all__"
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"
        
# class VendorAcceptDealSerializer(serializers.ModelSerializer):
#     accepted_vendor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     class Meta:
#         model = Purchase
#         fields = "__all__"
#     def update(self, instance, validated_data):
#         accepted_vendor = validated_data.pop("accepted_vendor")
#         instance.accepted_vendor_id = accepted_vendor.id
#         # instance.accepted_vendor = validated_data.get("email", instance.accepted_vendor)
#         instance.save()
#         return instance

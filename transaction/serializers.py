from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Transaction, Gas_Sizes, Card_details, Purchase

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
       
        

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"

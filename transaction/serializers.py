from rest_framework import serializers
from .models import Transaction, Gas_Sizes

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

class Gas_SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gas_Sizes
        fields = "__all__"

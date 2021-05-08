from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Transaction, Gas_Sizes, Card_details, Purchase
from user.models import User
from .serializers import TransactionSerializer, Gas_SizesSerializer, TransactionStatusSerializer, Card_detailsSerializer, PurchaseSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TransactionApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

class GasSizesViewSet(viewsets.ModelViewSet):
    queryset = Gas_Sizes.objects.all()
    serializer_class = Gas_SizesSerializer

class CardDetailsApiView(viewsets.ModelViewSet):
    queryset = Card_details.objects.all()
    serializer_class = Card_detailsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class PurchaseSerializerApiView(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    
    def perform_create(self, serializer):
        serializer.save(customer_id=self.request.user)

class CompletedTransactionAPiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        customer_name = Purchase.objects.filter(customer_id=self.request.user, transaction_completed=True).order_by("-created_at")
        serializer = TransactionStatusSerializer(instance=customer_name, many=True)

        return Response(serializer.data)

class UncompletedTransactionAPiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        customer_name = Purchase.objects.filter(customer_id=self.request.user, transaction_completed=False).order_by("-created_at")
        serializer = TransactionStatusSerializer(instance=customer_name, many=True)

        return Response(serializer.data)

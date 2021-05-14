from django.http.response import Http404
from rest_framework import response
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Transaction, Gas_Sizes, Card_details, Purchase
from user.models import User, Vendor_shop, Transporter
from .serializers import TransactionSerializer,  Gas_SizesSerializer, VendorAcceptDealSerializer, TransactionStatusSerializer, Card_detailsSerializer, PurchaseSerializer
from rest_framework.permissions import IsAuthenticated
import requests
import json



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
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
    
    def send_notification(self, request):
        
        url = "https://exp.host/--/api/v2/push/send"
        purchase_id = Purchase.objects.filter(customer=self.request.user).order_by('-id')[0]
        print(purchase_id)
        items = request.data["items_purchased"]
        customer_id = request.data["customer"]
        payload = json.dumps({
            "to": "ExponentPushToken[wQdLKrPsobAm5Nlq-E-yN1]",
            "sound": "default",
            "title": "New gas supply request",
            "body": f"Hello, I need this:\n\t{items}",
            "data": {
                "type": "requisition",
                "parameters": {
                "client_id": customer_id,
                },
                "requisition_params": {
                "id": purchase_id,
                "items": items
                }
            }
            })
        headers = {
            'Content-Type': 'application/json'
            }
        response = requests.request("POST", url, headers=headers, data=payload)
        return Response(response.text)
        

class CompletedTransactionAPiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        customer_name = Purchase.objects.filter(closest_vendor=self.request.user, transaction_completed=True).order_by("-created_at")
        serializer = TransactionStatusSerializer(instance=customer_name, many=True)

        return Response(serializer.data)

class UncompletedTransactionAPiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        customer_name = Purchase.objects.filter(closest_vendor=self.request.user, transaction_completed=False).order_by("-created_at")
        serializer = TransactionStatusSerializer(instance=customer_name, many=True)

        return Response(serializer.data)
    
class VendorAcceptDeal(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, format=None):
        vendor_accept = self.get_object(pk)
        serializer = VendorAcceptDealSerializer(vendor_accept, data=request.data)
        serializer.is_valid(raise_exception=True)
        accept = serializer.validated_data["accept"]
        if accept == True:
            vendor_name = Vendor_shop.objects.get(vendor=request.user)
            customer_purchase = Purchase.objects.get(pk=pk)
            customer_purchase.accepted_vendor = request.user
            customer_purchase.vendor_name = vendor_name
            customer_purchase.save()
            
            response = {
                "status_code":status.HTTP_200_OK,
                "Vendor_Accepted_deal":True,
                "items":customer_purchase.items_purchased,
                "item_cost":customer_purchase.item_cost,
                "distance": customer_purchase.distance,
                "total_cost":customer_purchase.total_price
            
            }
            return Response(response) 
        
        response={
            "Vendor_Accepted_deal": False
        }
        return Response(response)

class TransporterAcceptDeal(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist():
            raise Http404
    
    def put(self, request, pk, format=None):
        transporter_accept = self.get_object(pk)
        serializer = VendorAcceptDealSerializer(transporter_accept, data=request.data)
        serializer.is_valid(raise_exception=True)
        
        accept = serializer.validated_data["accept"]
        if accept == True:
            transporter = Transporter.objects.get(transporter=request.user)
            customer_purchase = Purchase.objects.get(pk=pk)
            customer_purchase.transporter = request.user
            customer_purchase.transporter_name = transporter
            customer_purchase.save()
        
        response = {
            "status_code":status.HTTP_200_OK,
            "Transporter_approval_status": "Accepted Delivery"
            
        }
        
        return Response(response)
            
            
        


    



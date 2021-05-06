from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import Vendor_shop_Serializer, Update_Device_Token_Serializer
from .models import Vendor_shop, User
from transaction.models import Transportation_cost_per_km
import math
from django.core.exceptions import ObjectDoesNotExist

def distance(lat1, lon1, lat2, lon2):

    #distance between latitudes and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    #convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    #apply formula
    a = (pow(math.sin(dLat / 2), 2) + pow(math.sin(dLon / 2), 2) * math.cos(lat1) * math.cos(lat2))

    radius = 6371
    c = 2 * math.asin(math.sqrt(a))
    distance = radius * c
    return distance


class VendorAPIView(APIView):
    serializer_class = Vendor_shop_Serializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Vendor_shop.objects.all()
        serializer = Vendor_shop_Serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        lat = serializer.validated_data["latitude"]
        long = serializer.validated_data["longitude"]
        
        try:
            delivery_unit_price = Transportation_cost_per_km.objects.get(pk=1)
            delivery_unit_price = delivery_unit_price.unit_price 
        except ObjectDoesNotExist:
            delivery_unit_price = 100

        vendors = Vendor_shop.objects.all()
        vendor = {}
        for vend in vendors:
            # vendor_list.append(vend)

            v_lat = vend.latitude
            v_long = vend.longitude
            dis = distance(lat, long, v_lat, v_long)
            # print(dis)
            if dis <= 5.0:
                vendor["vendor_id"] = vend.id
                vendor["Vendor_name"] = vend.company_name
                vendor["lat"] = vend.latitude
                vendor["long"] = vend.longitude
                vendor["address"] = vend.address
                vendor["distance"] = f"{dis}km"
                vendor["delivery_fee"] = math.ceil(dis) * delivery_unit_price
            # return Response({"Message":vendor}, status=status.HTTP_200_OK)
        # print(vendor_list)
        return Response({"Vendor":vendor}, status=status.HTTP_200_OK)


class Update_device_token(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = Update_Device_Token_Serializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        device_token = {'device_token':request.data.get("device_token")}
        serializer = self.serializer_class(request.user, data=device_token, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
        response = {
            'status_code': status.HTTP_200_OK,
            'Message':'Device token updated successfully',
            'Device_token':serializer.validated_data["device_token"]
        }
        return Response(response)

        



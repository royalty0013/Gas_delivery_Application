from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import VendorProfileSerializer
from .models import VendorProfile

class VendorAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = VendorProfile.objects.all()
        serializer = VendorProfileSerializer(queryset, many=True)
        return Response(serializer.data)

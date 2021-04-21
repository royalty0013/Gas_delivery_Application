from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Transaction, Gas_Sizes
from .serializers import TransactionSerializer, Gas_SizesSerializer
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
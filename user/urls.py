from django.urls import path
from .views import VendorAPIView

urlpatterns = [
    path('vendor-profile/', VendorAPIView.as_view(), name='vendor-profile' )
]
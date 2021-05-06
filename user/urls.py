from django.urls import path
from .views import VendorAPIView, Update_device_token

urlpatterns = [
    path('vendor/', VendorAPIView.as_view(), name='vendor' ),
    path('device-token/', Update_device_token.as_view(), name='device-token')
]
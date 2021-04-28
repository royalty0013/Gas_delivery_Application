from django.urls import path
from .views import VendorAPIView

urlpatterns = [
    path('vendor/', VendorAPIView.as_view(), name='vendor' )
]
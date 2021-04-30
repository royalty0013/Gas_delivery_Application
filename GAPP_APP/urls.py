"""GAPP_APP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from transaction.views import  GasSizesViewSet, CardDetailsApiView, PurchaseSerializerApiView

router = DefaultRouter()
router.register("gas-sizes", GasSizesViewSet)
router.register("card-detail", CardDetailsApiView)
router.register("customer-purchase", PurchaseSerializerApiView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/gateway/', include('gateway.urls')),
    path('api/', include('transaction.urls')),
    path('api/user/', include('user.urls')),
    path("api/gas/", include(router.urls)),
    path("api/card/", include(router.urls)),
    path("api/purchase/", include(router.urls))
    # path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset'))
]

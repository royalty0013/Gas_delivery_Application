from django.urls import path
from user.views import TransactionApiView

urlpatterns = [
    path("transaction/", TransactionApiView.as_view(), name="transaction")
]
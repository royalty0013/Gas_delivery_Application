from django.urls import path
from .views import TransactionApiView, CompletedTransactionAPiView, UncompletedTransactionAPiView, VendorAcceptDeal

urlpatterns=[
    path("transaction/", TransactionApiView.as_view(), name="transaction"),
    path("completed-transaction/", CompletedTransactionAPiView.as_view(), name="completed-transaction"),
    path("uncompleted-transaction/", UncompletedTransactionAPiView.as_view(), name="uncompleted-transaction"),
    path("vendor-accept-deal/<int:id>/", VendorAcceptDeal.as_view(), name="vendor-accept-deal")
]
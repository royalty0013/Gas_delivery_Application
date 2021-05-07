from django.urls import path
from .views import TransactionApiView, CompletedTransactionAPiView,UncompletedTransactionAPiView

urlpatterns=[
    path("transaction/", TransactionApiView.as_view(), name="transaction"),
    path("completed-transaction/", CompletedTransactionAPiView.as_view(), name="completed-transaction"),
    path("uncompleted-transaction/", UncompletedTransactionAPiView.as_view(), name="uncompleted-transaction"),
]
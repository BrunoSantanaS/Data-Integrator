from django.urls import path

from client_consumer.views import ClientTransactionViewSet

urlpatterns = [
    path('api/create/', ClientTransactionViewSet.as_view({'post': 'create'}), name='client-transaction-create'),
    path('api/list/', ClientTransactionViewSet.as_view({'get': 'list'}), name='client-transaction-list'),
]
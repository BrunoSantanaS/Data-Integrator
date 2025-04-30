from django.http import JsonResponse
from django.shortcuts import render
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from .models import ClientTransaction
from .serializer import ClientTransactionSerializer

# Create your views here.

class ClientTransactionViewSet(viewsets.ModelViewSet):
    @extend_schema(
        tags=['Client Transaction'],
        responses={200: ClientTransactionSerializer, 400: OpenApiTypes.OBJECT}
    )
    def list(self, request):
        """
        List all client transactions.
        """
        client_transactions = ClientTransaction.objects.all()
        serializer = ClientTransactionSerializer(client_transactions, many=True)
        return JsonResponse(serializer.data, safe=False)

    @extend_schema(
        tags=['Client Transaction'],
        request=ClientTransactionSerializer,
        responses={200: ClientTransactionSerializer, 400: OpenApiTypes.OBJECT}
    )
    def create(self, request):
        """
        Create a new client transaction.
        """
        serializer = ClientTransactionSerializer(data=request.data)
        if serializer.is_valid():
            client_transaction = ClientTransaction.objects.create(**serializer.validated_data)
            return JsonResponse({'message': 'Client transaction created successfully', 'client_transaction': client_transaction.id})
        else:
            return JsonResponse({'errors': serializer.errors}, status=400)

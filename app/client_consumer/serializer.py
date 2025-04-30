from rest_framework import serializers

from .models import ClientTransaction


class ClientTransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for ClientTransaction model.
    """
    transaction_type = serializers.CharField(max_length=100, required=True)
    client_name = serializers.CharField(max_length=100, required=True)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    date = serializers.DateTimeField(required=True)
    status = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = ClientTransaction
        fields = ['transaction_type', 'client_name', 'amount', 'date', 'status']
        extra_kwargs = {
            'transaction_type': {'validators': []},  # Disable default uniqueness validation
        }
        read_only_fields = ['transaction_type', 'client_name', 'amount', 'date', 'status']
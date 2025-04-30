from django.db import models

# Create your models here.


class ClientTransaction(models.Model):
    client_name = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

    class Meta:
        db_table = 'client_transaction'

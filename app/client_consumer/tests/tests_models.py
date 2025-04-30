from unittest import TestCase

from client_consumer.models import ClientTransaction


class ClientTransactionTest(TestCase):
    def setUp(self):
        ClientTransaction.objects.create(
            client_name="John Doe",
            transaction_type="Deposit",
            amount=100.00,
            date="2023-10-01",
            status="Completed"
        )

    def tearDown(self):
        ClientTransaction.objects.all().delete()

    def test_create_client_transaction(self):
        transaction = ClientTransaction.objects.get(client_name="John Doe")
        self.assertEqual(transaction.transaction_type, "Deposit")
        self.assertEqual(transaction.amount, 100.00)
        self.assertEqual(transaction.status, "Completed")

    def test_list_client_transactions(self):
        transactions = ClientTransaction.objects.all()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].client_name, "John Doe")
        self.assertEqual(transactions[0].transaction_type, "Deposit")

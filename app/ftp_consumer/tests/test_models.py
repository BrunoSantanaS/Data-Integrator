from django.test import TestCase

from ftp_consumer.models import FTPConnection


class FTPConnectionModelTest(TestCase):
    """
    Test case for the FTPConnection model.
    """

    def test_create_ftp_connection(self):
        """
        Test creating an FTP connection.
        """
        ftp_connection = FTPConnection.objects.create(
            host='ftp.example.com',
            port=21,
            username='user',
            password='password',
            directory='/path/to/directory'
        )
        self.assertEqual(ftp_connection.host, 'ftp.example.com')
        self.assertEqual(ftp_connection.port, 21)
        self.assertEqual(ftp_connection.username, 'user')
        self.assertEqual(ftp_connection.password, 'password')
        self.assertEqual(ftp_connection.directory, '/path/to/directory')

    def test_list_ftp_connections(self):
        """
        Test listing all FTP connections.
        """
        ftp_connection1 = FTPConnection.objects.create(
            host='ftp.example.com',
            port=21,
            username='user1',
            password='password1',
            directory='/path/to/directory1'
        )
        ftp_connection2 = FTPConnection.objects.create(
            host='ftp.example2.com',
            port=21,
            username='user2',
            password='password2',
            directory='/path/to/directory2'
        )
        ftp_connections = FTPConnection.objects.all()
        self.assertEqual(len(ftp_connections), 2)
        self.assertIn(ftp_connection1, ftp_connections)
        self.assertIn(ftp_connection2, ftp_connections)

    def test_delete_ftp_connection(self):
        """
        Test deleting an FTP connection.
        """
        ftp_connection = FTPConnection.objects.create(
            host='ftp.example.com',
            port=21,
            username='user',
            password='password',
            directory='/path/to/directory'
        )
        ftp_connection.delete()
        with self.assertRaises(FTPConnection.DoesNotExist):
            FTPConnection.objects.get(id=ftp_connection.id)

    def test_update_ftp_connection(self):
        """
        Test updating an FTP connection.
        """
        ftp_connection = FTPConnection.objects.create(
            host='ftp.example.com',
            port=21,
            username='user',
            password='password',
            directory='/path/to/directory'
        )
        ftp_connection.host = 'ftp.updated.com'
        ftp_connection.save()
        updated_ftp_connection = FTPConnection.objects.get(id=ftp_connection.id)
        self.assertEqual(updated_ftp_connection.host, 'ftp.updated.com')

    def test_get_ftp_connection_by_id(self):
        """
        Test getting an FTP connection by ID.
        """
        ftp_connection = FTPConnection.objects.create(
            host='ftp.example.com',
            port=21,
            username='user',
            password='password',
            directory='/path/to/directory'
        )
        retrieved_ftp_connection = FTPConnection.objects.get(id=ftp_connection.id)
        self.assertEqual(retrieved_ftp_connection, ftp_connection)

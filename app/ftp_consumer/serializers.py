from rest_framework import serializers

from .models import FTPConnection


class FTPConnectionSerializer(serializers.ModelSerializer):
    """
    Serializer for FTP connection details.
    """
    host = serializers.CharField(max_length=255, required=True)
    port = serializers.IntegerField(required=True)
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)
    directory = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = FTPConnection
        fields = ['host', 'port', 'username', 'password', 'directory']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        read_only_fields = ['id', 'created_at', 'updated_at']

from django.http import JsonResponse
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import viewsets

from .models import FTPConnection
from .serializers import FTPConnectionSerializer


# Create your views here.
class FtpConnectionViewSet(viewsets.ViewSet):
    """
    A viewset for handling FTP connections.
    """
    @extend_schema(
        tags=['FTP Connection'],
        responses={200: FTPConnectionSerializer, 400: OpenApiTypes.OBJECT}
    )
    def list(self, request):
        """
        List all FTP connections.
        """
        ftp_connections = FTPConnection.objects.all()
        serializer = FTPConnectionSerializer(ftp_connections, many=True)
        return JsonResponse(serializer.data, safe=False)

    @extend_schema(
        tags=['FTP Connection'],
        request=FTPConnectionSerializer,
        responses={201: FTPConnectionSerializer, 400: OpenApiTypes.OBJECT}
    )
    def create(self, request):
        """
        Create a new FTP connection.
        """
        serializer = FTPConnectionSerializer(data=request.data)
        if serializer.is_valid():
            ftp_connection = FTPConnection.objects.create(**serializer.validated_data)
            return JsonResponse({'message': 'FTP connection created successfully', 'ftp_connection': ftp_connection.id})
        else:
            return JsonResponse({'errors': serializer.errors}, status=400)

    @extend_schema(
        tags=['FTP Connection'],
        request=FTPConnectionSerializer,
        responses={200: FTPConnectionSerializer, 400: OpenApiTypes.OBJECT}
    )
    def destroy(self, request, pk=None):
        """
        Delete an FTP connection.
        """
        try:
            ftp_connection = FTPConnection.objects.get(pk=pk)
            ftp_connection.delete()
            return JsonResponse({'message': 'FTP connection deleted successfully'})
        except FTPConnection.DoesNotExist:
            return JsonResponse({'error': 'FTP connection not found'}, status=404)

    @extend_schema(
        tags=['FTP Connection'],
        request=FTPConnectionSerializer,
        responses={200: FTPConnectionSerializer, 404: OpenApiTypes.OBJECT}
    )
    def update(self, request, pk=None):
        """
        Update an FTP connection.
        """
        try:
            ftp_connection = FTPConnection.objects.get(pk=pk)
            serializer = FTPConnectionSerializer(ftp_connection, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'FTP connection updated successfully', 'ftp_connection': serializer.data})
            else:
                return JsonResponse({'errors': serializer.errors}, status=400)
        except FTPConnection.DoesNotExist:
            return JsonResponse({'error': 'FTP connection not found'}, status=404)

    @extend_schema(
        tags=['FTP Connection'],
        responses={200: FTPConnectionSerializer, 404: OpenApiTypes.OBJECT}
    )
    def retrieve(self, request, pk=None):
        """
        Retrieve an FTP connection by ID.
        """
        try:
            ftp_connection = FTPConnection.objects.get(pk=pk)
            serializer = FTPConnectionSerializer(ftp_connection)
            return JsonResponse(serializer.data, safe=False)
        except FTPConnection.DoesNotExist:
            return JsonResponse({'error': 'FTP connection not found'}, status=404)

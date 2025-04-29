from django.db import models
from django.utils import timezone


class FTPConnection(models.Model):
    host = models.CharField(max_length=255)
    port = models.IntegerField(default=21)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    directory = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ftp_connection'

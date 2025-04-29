from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from ftp_consumer.views import FtpConnectionViewSet

urlpatterns = [
    path('api/create/', FtpConnectionViewSet.as_view({'post': 'create'}), name='ftp-create'),
    path('api/list/', FtpConnectionViewSet.as_view({'get': 'list'}), name='ftp-connection-list'),
    path('api/delete/<int:pk>/', FtpConnectionViewSet.as_view({'delete': 'destroy'}), name='ftp-connection-delete'),
    path('api/update/<int:pk>/', FtpConnectionViewSet.as_view({'put': 'update'}), name='ftp-connection-update'),
    path('api/get/<int:pk>/', FtpConnectionViewSet.as_view({'get': 'retrieve'}), name='ftp-connection-detail'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
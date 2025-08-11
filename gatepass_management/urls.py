from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gatepass.api.urls')),  # Include API URLs
    path('', include('gatepass.urls')),  # Include Gate Pass app URLs
]
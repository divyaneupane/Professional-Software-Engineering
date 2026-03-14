from django.contrib import admin
from django.urls import path, include  # include is required for app URLs

urlpatterns = [
    path('admin/', admin.site.urls),       # Admin interface URL
    path('', include('bmi_app.urls')),     # Include app URLs here at the root of the project
]
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),  # Admin Panel
    path('', include('dashboard.urls')),  # Sare dashboard URLs yaha aa rahe hain
    path('oauth/', include('social_django.urls', namespace='social')),  # Social Login ke URLs
]

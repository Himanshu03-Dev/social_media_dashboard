from django.urls import path
from .views import register_view, login_view, logout_view, dashboard_view
from django.urls import path, include

urlpatterns = [
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('oauth/', include('social_django.urls', namespace='social')),
]
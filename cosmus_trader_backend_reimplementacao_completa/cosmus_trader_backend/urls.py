from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import RegisterView
from .views import home_view, login_view, LogoutView, RegisterView
from .views import profile_view
# Outras importações que você possa ter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='cosmos_trader_official'), name='logout'),
    path('', home_view, name='home'),
    path('accounts/profile/', profile_view, name='profile'),
]
from django.urls import path
from .views import IndexView, SignUpView, ProfileUpdateView, ProfileView
from django.contrib.auth import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(template_name="companies/login.html"), name='login'),
    path('logout/', views.LogoutView.as_view(template_name="companies/logout.html"), name='logout'),
    path('edit/', ProfileUpdateView.as_view(), name='edit'),
    path('show/<pk>/', ProfileView.as_view(), name='profile'),
]
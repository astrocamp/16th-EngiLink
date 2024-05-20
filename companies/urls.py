from django.urls import path
from .views import (
    CompanyHomeView,
    CompanyLoginView,
    CompanyLogoutView,
    CompanyDetailView,
    CompanyUpdateView,
    CompanyRegisterView, 
    CompanyPasswordChangeView,
    company_list,
)
from jobs import views as jobs

app_name = "companies"

urlpatterns = [
    path("", CompanyHomeView.as_view(), name="home"),
    path('register/', CompanyRegisterView.as_view(), name='register'),
    path("login/", CompanyLoginView.as_view(), name="login"),
    path("logout/", CompanyLogoutView.as_view(), name="logout"),
    path("password_change/",CompanyPasswordChangeView.as_view(),name="password_change",),
    path("<int:pk>/update/", CompanyUpdateView.as_view(), name="update"),
    path('<int:pk>/jobs/', jobs.IndexView.as_view(), name="jobs"),
    path('<int:pk>/create/', jobs.AddView.as_view(), name="jobs_create"),
    path("<int:pk>/", CompanyDetailView.as_view(), name="detail"),
    path('list/', company_list, name='company_list'),
]


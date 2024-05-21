from django.urls import path
from .views import (
    UserHomeView,
    UserLoginView,
    UserLogoutView,
    UserDetailView,
    UserUpdateView,
    UserRegisterView, 
    UserPasswordChangeView,
    ImportDataView,
    ApplyForJobView
)
from resumes import views as resumes

app_name = "users"

urlpatterns = [
    path("", UserHomeView.as_view(), name="home"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("password_change/",UserPasswordChangeView.as_view(),name="password_change",),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="update"),
    path("<pk>/resumes/", resumes.ResumeArea.as_view(), name="resumes"),
    path("<int:pk>/", UserDetailView.as_view(), name="detail"),
    path('import_data/', ImportDataView.as_view(), name='import_data'),
    path('apply/', ApplyForJobView.as_view(), name='apply_for_job'),
]
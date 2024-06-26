from django.urls import path
from resumes import views as resumes
from .views import (
    UserHomeView,
    UserLoginView,
    UserLogoutView,
    UserDetailView,
    UserUpdateView,
    UserRegisterView,
    UserPasswordChangeView,
    UserAddView,
    UserJobsView,
    ApplyForJobCreateView,
    ApplyForJobListView,
    WithdrawApplicationView,
    CollectJobView,
    InterviewResponseView,
    FavoriteCompaniesView,
    InterviewsCalendarView,
)

app_name = "users"

urlpatterns = [
    path("", UserHomeView.as_view(), name="home"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path(
        "password_change/",
        UserPasswordChangeView.as_view(),
        name="password_change",
    ),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="update"),
    path("<int:pk>/create/", UserAddView.as_view(), name="create"),
    path("<pk>/resumes/", resumes.ResumeArea.as_view(), name="resumes"),
    path("<int:job_id>/apply/", ApplyForJobCreateView.as_view(), name="apply"),
    path("<pk>/applied_jobs/", ApplyForJobListView.as_view(), name="applications"),
    path("<int:pk>/withdraw/", WithdrawApplicationView.as_view(), name="withdraw"),
    path("<int:pk>/", UserDetailView.as_view(), name="detail"),
    path("collect/", CollectJobView.as_view(), name="collect"),
    path("jobs/", UserJobsView.as_view(), name="jobs"),
    path('interview/<int:pk>/', InterviewResponseView.as_view(), name='interview'),
    path('calendar/', InterviewsCalendarView.as_view(), name='calendar'),
    path("favorites/", FavoriteCompaniesView.as_view(), name="favorites"),
]

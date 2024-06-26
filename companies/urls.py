from django.urls import path
from .views import (
    CompanyHomeView,
    CompanyLoginView,
    CompanyLogoutView,
    CompanyDetailView,
    CompanyUpdateView,
    CompanyRegisterView,
    CompanyPasswordChangeView,
    CompanyListView,
    CompanyInfoView,
    CollectCompanyView,
    JobApplicationsView,
    JobApplicationDetailView,
    MarkAsReadView,
    InterviewResultCreateView,
    FavoriteCompanyView,
    CompanyInterviewsCalendarView
)
from jobs import views as jobs

app_name = "companies"

urlpatterns = [
    path("", CompanyHomeView.as_view(), name="home"),
    path("list/", CompanyListView.as_view(), name="company_list"),
    path("info/<int:pk>/", CompanyInfoView.as_view(), name="company_info"),
    path("register/", CompanyRegisterView.as_view(), name="register"),
    path("login/", CompanyLoginView.as_view(), name="login"),
    path("logout/", CompanyLogoutView.as_view(), name="logout"),
    path(
        "password_change/",
        CompanyPasswordChangeView.as_view(),
        name="password_change",
    ),
    path("<int:pk>/update/", CompanyUpdateView.as_view(), name="update"),
    path("<int:pk>/jobs/", jobs.IndexView.as_view(), name="jobs"),
    path("<int:pk>/create/", jobs.AddView.as_view(), name="jobs_create"),
    path("<int:pk>/applications/", JobApplicationsView.as_view(), name="applications"),
    path("<int:pk>/mark", MarkAsReadView.as_view(), name="mark"),
    path("<int:pk>/", CompanyDetailView.as_view(), name="detail"),
    path(
        "<int:job_resume_id>/interview/",
        InterviewResultCreateView.as_view(),
        name="interview",
    ),
    path("<int:pk>/candidate/", JobApplicationDetailView.as_view(), name="candidate"),
    path("companies/<int:company_id>/favorite/", FavoriteCompanyView.as_view(), name="favorite_company"),
    path("<int:company_id>/collect/", CollectCompanyView.as_view(), name="collect_company"),
    path('calendar/', CompanyInterviewsCalendarView.as_view(), name='calendar'),
]

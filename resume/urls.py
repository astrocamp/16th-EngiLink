from django.urls import path
from .views import ResumeArea,MyResume,ProfileListView,ProfileCreateView,ProfileUpdateView,ProfileDeleteView

app_name = 'resume'  # 定義 app_name

urlpatterns = [
    path('',ResumeArea.as_view(),name='ResumeArea'),
    path('MyResume/',MyResume.as_view(),name='MyResume'),
    path('ProfileShow/',ProfileListView.as_view(),name='ProfileShow'),
    path('ProfileCreate/',ProfileCreateView.as_view(),name='ProfileCreate'),
    path('ProfileUpdate/<pk>', ProfileUpdateView.as_view(), name='ProfileUpdate'),
    path('ProfileDeleteView/<pk>', ProfileDeleteView.as_view(), name='ProfileDeleteView'),
]
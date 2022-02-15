from django.contrib import admin
from django.urls import path, include
from main import views
import resumeuploader.settings

urlpatterns = [
    
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>', views.CandidateView.as_view(), name='candidate')
    
]

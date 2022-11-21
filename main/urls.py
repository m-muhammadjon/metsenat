from django.urls import path
from main import views

urlpatterns = [
    path('sponsor/', views.SponsorView.as_view()),
]

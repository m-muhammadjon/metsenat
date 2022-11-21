from django.urls import path

from main import views

urlpatterns = [
    path('sponsor/', views.SponsorView.as_view()),
    path('sponsor/<int:pk>/', views.SponsorDetailView.as_view()),
]

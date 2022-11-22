from django.urls import path

from main import views

urlpatterns = [
    path('sponsor/', views.SponsorView.as_view()),
    path('sponsor/<int:pk>/', views.SponsorDetailView.as_view()),
    path('university/', views.UniversityView.as_view()),
    path('student/', views.StudentView.as_view()),
    path('student/<int:pk>/', views.StudentDetailView.as_view()),
    path('donation/', views.DonationView.as_view()),
    path('dashboard/', views.DashboardView.as_view()),
]

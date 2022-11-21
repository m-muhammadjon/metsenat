from django.contrib import admin
from django.urls import path, include
from backend.swagger import urlpatterns as swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1', include('backend.routing')),
]
urlpatterns += swagger_urls

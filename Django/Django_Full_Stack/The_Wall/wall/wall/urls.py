from django.urls import path, include

urlpatterns = [
    path('', include('loginapp.urls')),
    path('wall', include('wallapp.urls')),
]

from django.urls import path, include

urlpatterns = [
    path('', include ('ormapp.urls')),
]
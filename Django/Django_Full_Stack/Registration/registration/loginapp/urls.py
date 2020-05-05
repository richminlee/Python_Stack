from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login',views.login),
    path('success/<int:userid>',views.success),
    path('success2/<int:userid>',views.success2),
    path('logout',views.logout)
]
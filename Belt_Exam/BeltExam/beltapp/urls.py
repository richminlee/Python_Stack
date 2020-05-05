from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('quotes',views.quotes),
    path('quotes/users/<int:userid>',views.user),
    path('myaccount/<int:userid>',views.edit),
    path('quotes/<int:quoteid>/delete',views.delete),
    path('quotes/add',views.add),
    path('register', views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('like/<int:quoteid>',views.like)
]
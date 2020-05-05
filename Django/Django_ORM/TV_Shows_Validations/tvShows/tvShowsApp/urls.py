from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.addShow),
    path('newShow',views.newShow),
    path('shows/<int:showid>', views.showinfo),
    path('shows/<int:showid>/edit', views.edit),
    path('shows/<int:showid>/delete',views.delete)
]
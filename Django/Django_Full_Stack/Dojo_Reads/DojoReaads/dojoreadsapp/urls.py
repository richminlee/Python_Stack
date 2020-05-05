from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('books',views.books),
    path('books/add',views.add),
    path('books/<int:bookid>',views.onebook),
    path('books/<int:revid>/<int:bookid>/delete',views.delete),
    path('books/users/<int:userid>',views.users),
    path('register', views.register),
    path('login',views.login),
    path('logout',views.logout)
]
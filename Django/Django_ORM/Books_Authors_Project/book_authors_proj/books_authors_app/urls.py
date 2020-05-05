from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('addBook', views.addBook),
    path('authors',views.Authors),
    path('addAuthor', views.addAuthor),
    path('books/<int:bookid>',views.bookInfo),
    path('author/<int:authorid>',views.authorInfo)
]
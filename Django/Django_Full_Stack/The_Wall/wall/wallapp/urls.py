from django.urls import path
from . import views
urlpatterns = [
    path('',views.wallie),
    path('/<int:messid>',views.delete),
    path('/<int:messid>/comment',views.comment),
    path('/<int:messid>/comdel',views.comdel)
]
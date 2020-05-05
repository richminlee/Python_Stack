from django.db import models
from loginapp.models import loginManager, Login

class Message(models.Model):
    messagess = models.TextField()
    logged = models.ForeignKey(Login, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comments = models.TextField()
    messages = models.ManyToManyField(Message, related_name = "comments",)
    logged = models.ForeignKey(Login, related_name="comment", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
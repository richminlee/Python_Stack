from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'table':user.objects.all()
    }
    return render(request, "index.html", context)

def addUser(request):
    user.objects.create(first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        email_address=request.POST['email'],
                        age=request.POST['agey'],
    )
    return redirect("/")
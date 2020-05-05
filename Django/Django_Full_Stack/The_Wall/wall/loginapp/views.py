from django.shortcuts import render, redirect
from loginapp.models import *
from django.contrib import messages
import bcrypt



def index(request):
    return render(request, "index.html")

def register(request):
    errors = Login.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect ('/')
    else: 
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        logged = Login.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            birthdate = request.POST['birthdate'],
            email = request.POST['email'],
            password = pw_hash
        )
        request.session['logged_id'] = logged.id
        return redirect(f'/wall')

def login(request):
    user = Login.objects.filter(email=request.POST['email'])
    if user:
        logged = user[0]

        if bcrypt.checkpw(request.POST['password'].encode(), logged.password.encode()):
            request.session['logged_id'] = logged.id
            return redirect('/wall')
    messages.error(request,"Invalid email/password", extra_tags="login")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect("/")
from django.shortcuts import render, redirect
from .models import *
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
        Login.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            birthdate = request.POST['birthdate'],
            email = request.POST['email'],
            password = pw_hash
        )
        a=Login.objects.get(email=request.POST['email'])
        userid=a.id
        return redirect(f'/success/{userid}')

def login(request):
    user = Login.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['email'] = logged_user.email
            a=Login.objects.get(email=request.POST['email'])
            userid=a.id
            return redirect(f'/success2/{userid}')
    return redirect('/')

def success(request,userid):
    if userid not in request.session:
        return redirect('/')
    context = {
        'success' : Login.objects.get(id = userid),
    }
    return render(request,"success.html", context)

def success2(request,userid):
    if userid not in request.session:
        return redirect('/')
    context = {
        'success' : Login.objects.get(id = userid),
    }
    return render(request,"success2.html", context)
def logout(request):
    try:
        del request.session['email']
        del request.session['password']
    except KeyError:
        pass
    return redirect("/")
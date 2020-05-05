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
        logged = Login.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        request.session['logged_id'] = logged.id
        return redirect('/quotes')

def login(request):
    user = Login.objects.filter(email=request.POST['email'])
    if user:
        logged = user[0]

        if bcrypt.checkpw(request.POST['password'].encode(), logged.password.encode()):
            request.session['logged_id'] = logged.id
            return redirect('/quotes')
    messages.error(request,"Invalid email/password", extra_tags="login")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect("/")

def quotes(request):
    if 'logged_id' not in request.session:
        return redirect('/')
    
    context = {
        'user': Login.objects.get(id=request.session['logged_id']),
        'quotes': Quote.objects.all(),
        'likes': Like.objects.all()
    }
    return render(request, 'quotes.html',context)
def add(request):
    if 'logged_id' not in request.session:
        return redirect('/')
    if request.method == 'POST':
        errors = Quote.objects.quote_val(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/quotes')
        Quote.objects.create(
            logged=Login.objects.get(id=request.session['logged_id']),
            quotes=request.POST['quotes'], 
            author=request.POST['author'],
            )
        return redirect('/quotes')
def user(request,userid):
    if 'logged_id' not in request.session:
        return redirect('/')
    users = Login.objects.get(id=userid)
    context = {
        'user': Login.objects.get(id=userid),
        'quotes' : Quote.objects.filter(logged=users)
    }
    return render(request,'users.html',context)
def edit(request,userid):
    if 'logged_id' not in request.session:
        return redirect('/')
    if request.method=="POST":
        errors = Login.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect (f"/myaccount/{userid}")
        else: 
            c=Login.objects.get(id=userid)
            c.first_name = request.POST["first_name"]
            c.last_name=request.POST["last_name"]
            c.email=request.POST["email"]
            c.password=c.password
            c.save()
            return redirect("/quotes")
    context = {
        'user': Login.objects.get(id=userid)
    }
    return render(request,'myaccount.html',context)

def delete(request,quoteid):
    d = Quote.objects.get(id=quoteid)
    d.delete()
    return redirect("/quotes")
def like(request,quoteid):
    Like.objects.create(
        quotes = Quote.objects.get(id=quoteid),
        logged = Login.objects.get(id=request.session['logged_id']),
        yes = 1
    )
    return redirect('/quotes')
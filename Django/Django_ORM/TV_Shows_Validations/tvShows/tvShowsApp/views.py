from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    return redirect("/shows")

def shows(request):
    context = {
        'table' : show.objects.all()
    }
    return render(request, "index.html", context)

def addShow(request):
    return render(request,"new.html")

def newShow(request):
    errors = show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect ('/shows/new')
    else:    
        show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],   
            description = request.POST['description'],
        )
        a=show.objects.get(title=request.POST['title'])
        showid=a.id
        return redirect(f"/shows/{showid}")

def showinfo(request,showid):
    context = {
        'showinfo':show.objects.get(id=showid)
    }
    return render(request, "shows.html",context)

def edit(request,showid):
    if request.method=="POST":
        errors = show.objects.basic_validatory(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect (f"/shows/{showid}/edit")
        else:  
            c=show.objects.get(id=showid)
            c.title = request.POST["title"]
            c.network=request.POST["network"]
            c.release_date=request.POST["release_date"]
            c.description=request.POST["description"]
            c.save()
            return redirect(f"/shows/{showid}")
    context = {
        'showinfo':show.objects.get(id=showid)
    }
    return render(request,"edit.html", context)

def delete(request,showid):
    d=show.objects.get(id=showid)
    d.delete()
    return redirect("/shows")
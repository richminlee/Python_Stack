from django.shortcuts import render, redirect
from .models import *
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
    show.objects.create(
        title = request.POST['titlen'],
        network = request.POST['networkn'],
        release_date = request.POST['release_daten'],   
        description = request.POST['descriptionn'],
    )
    a=show.objects.get(title=request.POST['titlen'])
    showid=a.id
    return redirect(f"/shows/{showid}")

def showinfo(request,showid):
    context = {
        'showinfo':show.objects.get(id=showid)
    }
    return render(request, "shows.html",context)

def edit(request,showid):
    if request.method=="POST":
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
from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'table':books.objects.all()
    }
    return render(request, "index.html", context)

def addBook(request):
    books.objects.create(title = request.POST["title"],
                        desc = request.POST["desc"],
    )
    return redirect("/")

def Authors(request):
    context = {
        'table':authors.objects.all()
    }
    return render(request, "authors.html", context)
def addAuthor(request):
    authors.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes'],
    )
    return redirect("/authors")
def bookInfo(request,bookid):
    if request.method=='POST':
        this_book=books.objects.get(id=bookid)
        this_author=authors.objects.get(first_name=request.POST['autho'])
        this_book.author.add(this_author)
    context = {
        'bookie':books.objects.get(id=bookid),
        'auth': authors.objects.all()
    }
    return render(request,"books.html", context)
def authorInfo(request,authorid):
    if request.method=='POST':
        this_author=authors.objects.get(id=authorid)
        this_book=books.objects.get(title=request.POST['bookk'])
        this_author.books.add(this_book)
    context = {
        'authie':authors.objects.get(id=authorid),
        'boo': books.objects.all()
    }
    return render(request,"authorinfo.html", context)
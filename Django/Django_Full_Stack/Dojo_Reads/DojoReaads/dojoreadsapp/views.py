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
            alias = request.POST['alias'],
            birthdate = request.POST['birthdate'],
            email = request.POST['email'],
            password = pw_hash
        )
        request.session['logged_id'] = logged.id
        return redirect('/books')

def add(request):

    if 'logged_id' not in request.session:
        return redirect('/')

    if request.method == 'POST':
        errors = Book.objects.book_val(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/books/add')
        Book.objects.create(
            logged=Login.objects.get(id=request.session['logged_id']),
            title=request.POST['title'], 
            author=request.POST['author'],
            )
        Review.objects.create(
            logged=Login.objects.get(id=request.session['logged_id']),
            review = request.POST['review'],
            rating = request.POST['rating']
        )
        book=Book.objects.get(title=request.POST['title'])
        bookid=book.id
        
        this_review = Review.objects.get(review=request.POST['review'])
        book.review.add(this_review)
        return redirect(f'/books/{bookid}')
    context = {
        'bookie': Book.objects.all(),
    }
    return render(request, 'addbook.html',context)
    

def books(request):

    context = {
        'user': Login.objects.get(id=request.session['logged_id']),
        'books': Book.objects.all()
    }
    return render(request,'books.html',context)

def onebook(request,bookid):
    if request.method == 'POST':
        Review.objects.create(
            logged=Login.objects.get(id=request.session['logged_id']),
            review = request.POST['review'],
            rating = request.POST['rating']
        )
        book=Book.objects.get(id=bookid)
        bookid=book.id
    
        this_review = Review.objects.get(review=request.POST['review'])
        book.review.add(this_review)

        return redirect(f'/books/{bookid}')
    book = Book.objects.get(id=bookid)
    context = {
        'book': Book.objects.get(id=bookid),
        'review': book.review.all()
    }
    return render(request,'onebook.html',context)

def users(request,userid):
    users = Login.objects.get(id=userid)
    context = {
        'user': Login.objects.get(id=userid),
        'books' : Book.objects.filter(logged=users)
    }
    return render(request,'users.html',context)

def login(request):
    user = Login.objects.filter(email=request.POST['email'])
    if user:
        logged = user[0]

        if bcrypt.checkpw(request.POST['password'].encode(), logged.password.encode()):
            request.session['logged_id'] = logged.id
            return redirect('/books')
    messages.error(request,"Invalid email/password", extra_tags="login")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect("/")

def delete(request,revid,bookid):
    d = Review.objects.get(id=revid)
    d.delete()
    return redirect(f"/books/{bookid}")
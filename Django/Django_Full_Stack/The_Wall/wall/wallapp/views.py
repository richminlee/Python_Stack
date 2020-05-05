from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

def wallie(request):
    if 'logged_id' not in request.session:
        return redirect('/')
    
    if request.method == "POST":
        Login.objects.get(id=request.session['logged_id'])
        Message.objects.create(
            messagess = request.POST['messages'],
            logged_id = request.session['logged_id']
            )
    context = {
        'messages' : Message.objects.all().order_by("-id"),
        'logged' : Login.objects.get(id=request.session['logged_id']),
    }
    return render(request, 'wallie.html', context)
def delete(request,messid):
    if request.session['logged_id'] == Message.objects.get(id=messid).logged_id:
        d = Message.objects.get(id=messid)
        d.delete()
        return redirect("/wall")
    else:
        return redirect("/wall")

def comment(request,messid):
    if 'logged_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        Comment.objects.create(
            comments = request.POST['com'],
            logged_id = request.session['logged_id']
            )
        this_message = Message.objects.get(id=messid)
        this_comment = Comment.objects.get(comments = request.POST['com'])
        this_message.comments.add(this_comment)
    return redirect("/wall")

def comdel(request,messid):
    if request.session['logged_id'] == Comment.objects.get(id=messid).logged_id:
        d = Comment.objects.get(id=messid)
        d.delete()
        return redirect("/wall")
    else:
        return redirect("/wall")
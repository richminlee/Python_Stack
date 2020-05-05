from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
def index(request):
    if request.method== "GET":
        request.session["counter1"]=1
    elif request.method=="POST":
        request.session["counter1"]+=1
    randomWord = get_random_string(length=14)

    context  = {
        "random" : randomWord,
        "count" : request.session["counter1"]
    }
    return render(request,"index2.html", context)
def reset(request):
    request.session.clear()
    return redirect("/random_word")
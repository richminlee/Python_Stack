from django.shortcuts import render, redirect
def index(request):
    return render(request,"index.html")
def create_user(request):
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    comment_form = request.POST['comment']

    context = {
        "name_on_template" : name_from_form,
        "location_on_template" : location_from_form,
        "language_on_template" : language_from_form,
        "comment_on_template" : comment_form,
    }
    return render(request,"success.html", context)

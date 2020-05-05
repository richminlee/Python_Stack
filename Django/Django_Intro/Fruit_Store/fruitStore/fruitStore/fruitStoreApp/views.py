from django.shortcuts import render, redirect
def index(request):
    return render(request, "index.html")
def checkout(request):
    firstName_form = request.POST['first_name']
    lastName_form = request.POST['last_name']
    sid_form = request.POST['student_id']
    straw_form=request.POST['strawberry']
    rasp_form=request.POST['raspberry']
    apple_form=request.POST['apple']
    total = int(straw_form)+int(rasp_form)+int(apple_form)
    cust = firstName_form+lastName_form
    context = {
        "firstName_template" : firstName_form,
        "lastName_template" : lastName_form,
        "sid_template" : sid_form,
        "straw_template" : straw_form,
        "rasp_template" : rasp_form,
        "apple_template" : apple_form,
        "total_temp" : total
    }
    print(f"Charging {cust} for {total} fruits")
    return render(request, "checkout.html", context)
def fruits(request):
    return render(request, "fruits.html")
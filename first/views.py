from django.shortcuts import render,redirect
from .models import *

def home(request):
    return render(request, 'home.html')

def survay(request):
    if request.method == "POST":
        Survey.objects.create(
            name=request.POST.get("name"),
            contact=request.POST.get("contact"),
            message=request.POST.get("message")
        )
    return redirect("/")

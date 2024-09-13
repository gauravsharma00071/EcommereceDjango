from django.shortcuts import render
from django.contrib import messages
from ecommerceapp.models import Contact

# Create your views here.

def index(request):
    return render(request,"index.html")

def contact(request):
    if request.method =="POST":
        name=request.POST.get("fullName")
        email=request.POST.get("inputEmail")
        desc=request.POST.get("desc")
        phonenumber=request.POST.get("inputNumber")
        myquery=Contact(name=name,email=email,desc=desc,phonenumber=phonenumber)
        myquery.save()
        messages.info(request,"We will get back you to soon...")
        return render(request,contact.html)
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

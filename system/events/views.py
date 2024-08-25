from django.contrib import messages
from django.shortcuts import redirect, render

from .models import User

def register(request):
    return render(request,"Signup.html")

def insert_data(request):
    if request.method == "POST":
       name=request.POST.get("Name")
       email=request.POST.get("Email")
       password=request.POST.get("upasssword")
       phone=request.POST.get("uphone")
       queary= User.objects.filter(email=email)
       if queary.exists():
          messages.error(request,'Email Already Exists!!')
          return render(request,"Signup.html")
       else:
           queary=User(Name=name,contactno=phone,email=email,password=password)
           queary.save()
           messages.success(request,'REGISTRATION SUCUESSFUL!!')
           return render(request,"Login.html")
    else:
        messages.error(request,'SORRY!! UNABLE TO REEQUEST')
        return render(request,"Signup.html")

from django.contrib import messages
from django.shortcuts import redirect, render

from .models import User

def register(request):
    return render(request,"Signup.html")

def login(request):
    return render(request,"Login.html")

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
    
def CheckLogin(request):
    useremail=request.POST['Email']
    userpwd=request.POST['Password']
    try:
        query=User.objects.get(email=useremail,password=userpwd)
        request.session['useremail']=query.email
        request.session['user_id'] = query.id
        request.session.save()
        print(request.session['user_id'])
    except User.DoesNotExist:
        query=None
    if query is None:
        messages.info(request, 'Account Does Not Exists !! Please Sign Up')
        return render(request, "Signup.html")
    else:
        messages.success(request,'LOGIN SUCCESSFUL!!')
    return render(request,"index.html")

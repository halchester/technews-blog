from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signupPage(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User created successfully")
            return redirect('login')
    context = {"form":form}
    return render(request,'accounts/signup.html',context)

def loginPage(request):
    context = {}
    return render(request,'accounts/login.html',context)

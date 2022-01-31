from django.core import paginator
from django.shortcuts import render, redirect
from .models import Order, Products
from django.core.paginator import Paginator
from .form import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import ProjectForm, ProfileForm
# Create your views here.

@login_required(login_url="login")
def additem(request):
    
    form = ProjectForm()
    
    if request.method == 'POST':
         form = ProjectForm(request.POST, request.FILES)
         if form.is_valid():
            form.save()
             
    context = {'form':form}
    return render(request,'form.html', context)

@login_required(login_url="login")
def editItem(request, pk):
    product_objects = Products.objects.get(id=pk)
    form = ProjectForm(instance=product_objects)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=product_objects)
        if form.is_valid:
            form.save()
            return redirect("index")
        
    
    return render(request,'form.html', {'form':form})

@login_required(login_url="login")
def deleteItem(request, pk):
    product_objects = Products.objects.get(id=pk)
    product_objects.delete()
        
    return redirect("index")


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')
    form = ProfileForm()
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)  
        except:
            messages.error(request,"User name does not exist")
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('index')
        else:
            messages.error(request,"Username or password is incorrect!")
            

              
    context = {'form':form, 'page':page}
    return render(request, 'login_register.html', context)

@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('index')

def registerUser(request):
    page = 'register'    
    form =  CustomUserCreationForm()
    
    if request.method =='POST':        
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
          print("Something Wrong")

            
    context = {'page':page, 'form':form}
    return render(request, 'login_register.html',context)


from django.core import paginator
from django.shortcuts import render, redirect
from .models import Products
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

def index(request):
    product_objects = Products.objects.all()
    template_name = 'index.html'
    # Search funtionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:                           
        product_objects =product_objects.filter(title__icontains = item_name) 

    #Paginator code & link 
    #https://docs.djangoproject.com/en/3.2/topics/pagination/
    paginator = Paginator(product_objects,4)
    page_number = request.GET.get('page')
    product_objects = paginator.get_page(page_number)

    return render(request,template_name,{'product_objects': product_objects})


def detail(request,pk):
    product_objects = Products.objects.get(id=pk)
    return render(request,'detail.html',{'product_objects':product_objects})

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


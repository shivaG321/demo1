from django.shortcuts import render, redirect
from .forms import ProductModelForm
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def homeview(request):
    template_name = 'Sellerapp/home.html'
    context = {}
    return render(request, template_name, context)


@login_required(login_url='signin')
def addprodcutview(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            print('before return')
            return redirect('showprod')

    template_name = 'Sellerapp/addproduct.html'
    context = {'form':form}
    return render(request, template_name, context)

def showproductviews(request):
    template_name = 'Sellerapp/showprod.html'
    prods = Product.objects.all()
    context = {'prods': prods}
    return render(request, template_name, context)

def updateproductview(request,id):
    prod_object = Product.objects.get(id=id)
    form = ProductModelForm(instance=prod_object)
    if request.method == 'POST':
        form = ProductModelForm(request.POST, instance=prod_object)
        if form.is_valid():
            form.save()
            return redirect('showprod')
    template_name = 'Sellerapp/addproduct.html'
    context = {'form': form, 'btn_name': 'Update_Product'}
    return render(request, template_name, context)

def deleteproductview(request,id):
    prod = Product.objects.get(id=id)
    if request.method == 'POST':
        prod.delete()
        return redirect('showprod')
    template_name = 'Sellerapp/delete.html'
    context = {'prod': prod}
    return render(request, template_name, context)


def signupview(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    template_name = 'Sellerapp/signup.html'
    context = {'form': form}
    return render(request, template_name, context)

def signinview(request):
    if request.method == 'POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('showprod')
        else:
            messages.error(request, 'invalid password,plz enter correct Username and Password..!')

    template_name = 'Sellerapp/signin.html'
    context = {}
    return render(request, template_name, context)

def signoutview(request):
    logout(request)
    return redirect('signin')
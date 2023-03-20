from django.shortcuts import render

# Create your views here.

def base(request):
    context = {}
    return render(request, 'pets/base.html', context)

def home(request):
    context = {}
    return render(request, 'pets/home.html', context)

def cart(request):
    context = {}
    return render(request, 'pets/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'pets/checkout.html', context)

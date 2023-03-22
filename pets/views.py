from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

def base(request):
    context = {}
    return render(request, 'pets/base.html', context)

def home(request):
    context = {}
    return render(request, 'pets/home.html', context)

def about(request):
    context = {}
    return render(request, 'pets/about.html', context)

def cart(request):
    context = {}
    return render(request, 'pets/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'pets/checkout.html', context)


from pets.forms import CategoryForm
from pets.forms import PageForm
from pets.models import Category, Page

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('home')  # Redirect to the home view
        else:
            print(form.errors)

    return render(request, 'pets/add_category.html', {'form': form})

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'pets/category.html', context_dict)

@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.save()
                return redirect('home')  # Redirect to the home view after successfully saving the page
        else:
            print(form.errors)
    else:
        form = PageForm()

    context = {'form': form, 'category': category}
    return render(request, 'pets/add_page.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'pets/login.html', {})


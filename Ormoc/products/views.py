from itertools import product
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
from .forms import SignupForm
from .models import Product



def main(request):
    context = {}
    return render(request, 'products/main.html', context)

def home(request):
    context = {}
    return render(request, 'products/home.html', context)

def logouut(request):
    context = {}
    return render(request, 'registration/logouut.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})

from django.contrib.auth.models import User

def get_all_users(request):
    all_users = User.objects.all()
    # Do something with the all_users queryset
    return render(request, 'products/users_template.html', {'all_users': all_users})

def display_users(request):
    all_users = User.objects.all()
    return render(request, 'products/users_template.html', {'all_users': all_users})

def Product(request):
    product = Product.objects.all()
    return render(request, 'products/home.html', {'home': Product})


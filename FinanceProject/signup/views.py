from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm, UserForm
from django.contrib import messages



# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/intake')
    else:
        form = RegisterForm()
    return render(request, 'signup/register.html', {'form': form})

def custom_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/welcome')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form= LoginForm()
    return render(request, 'signup/login.html', {'form': form})
    

def custom_logout_view(request):
    logout(request)
    return redirect('/login')

def questionaireform(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/welcome')
    else:
        form = UserForm()

    return render(request, 'questionaire.html', {'form': form})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import RegisterForm


# Create your views here.
def signup(request):
    return HttpResponse("Create an account")

def questionaire(request):
    return HttpResponse("An assorted array of questions")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/welcome')
    else:
        form = RegisterForm()
    return render(request, 'signup/register.html', {'form': form})
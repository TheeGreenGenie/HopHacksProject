from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    return render(request, 'home.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def buy(request):
    return render(request, 'buy.html')

def reccomendations(request):
    return render(request, 'reccomendations.html')

def sell(request):
    return render(request, 'sell.html')

def transactions(request):
    return render(request, 'transactions.html')

def profit(request):
    return render(request, 'profit.html')

def settings(request):
    return render(request, 'settings.html')

def profile(request):
    return render(request, 'profile.html')
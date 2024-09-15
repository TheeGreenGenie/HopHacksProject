from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from signup.models import UserData
from MainPage.model_code import charts

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

    current_username = request.user.username

    user_data = get_object_or_404(UserData, username=current_username)

    return render(request, 'profile.html', {'user_data': user_data})

def user_data_view(request):

    current_username = request.user.username

    user_data = get_object_or_404(UserData, username=current_username)

    return render(request, 'welcome.html', {'user_data': user_data, 'charts': charts})


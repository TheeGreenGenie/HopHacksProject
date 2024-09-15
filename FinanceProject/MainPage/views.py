from django.shortcuts import render, get_object_or_404
from MainPage import moving_graphs, volume, model_code, more_yfinance, Rsi
from signup.models import UserData
import base64
import io


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    return render(request, 'home.html')

def performers(request):

    df_html = more_yfinance.df.to_html(classes='table table-striped')

    return render(request, 'performers.html', {'df_html': df_html})

def buy(request):
    return render(request, 'buy.html')


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

    return render(request, 'welcome.html', {'user_data': user_data, 'charts': model_code.charts})


def stock_analysis(request):

    return render(request, 'stock_analysis.html', {'graph1': moving_graphs.graph1, 'graph2': volume.graph2, 'graph3': Rsi.graph3})
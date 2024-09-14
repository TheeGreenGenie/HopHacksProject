from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome')

def home(request):
    return HttpResponse('Home Page')

def portfolio(request):
    return HttpResponse("Portfolio Page")

def buy(request):
    return HttpResponse("Buy Stocks")

def reccomendations(request):
    return HttpResponse("Stock reccommendations")

def sell(request):
    return HttpResponse("Sell Stocks")

def transactions(request):
    return HttpResponse("Trasnsaction History")

def profit(request):
    return HttpResponse("Losses and Gains")

def settings(request):
    return HttpResponse("Settings page")
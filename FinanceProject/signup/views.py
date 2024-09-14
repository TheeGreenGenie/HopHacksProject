from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup(request):
    return HttpResponse("Create an account")

def questionaire(request):
    return HttpResponse("An assorted array of questions")
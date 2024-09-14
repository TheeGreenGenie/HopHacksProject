"""
URL configuration for FinanceProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from MainPage import views as mainviews
from signup import views as signviews
from signup import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup/", signviews.signup),
    path("welcome/", mainviews.welcome),
    path("portfolio/", mainviews.portfolio),
    path("buy/", mainviews.buy),
    path("reccomendations/", mainviews.reccomendations),
    path("sell/", mainviews.sell),
    path("transactions/", mainviews.transactions),
    path("profit/", mainviews.profit),
    path("settings/", mainviews.settings),
    path("home/", mainviews.home),
    path("profile/", mainviews.profile),
    path('register/', auth_views.register),
    path('', include('django.contrib.auth.urls'))
]

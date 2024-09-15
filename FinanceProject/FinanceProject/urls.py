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
    path("welcome/", mainviews.user_data_view),
    path("performers/", mainviews.performers),
    path("stock_analysis/", mainviews.stock_analysis),
    path("settings/", mainviews.settings),
    path("home/", mainviews.home),
    path("profile/", mainviews.profile),
    path('', auth_views.register),
    path('intake/', signviews.questionaireform),
    path('login/', signviews.custom_login_view),
    path('logout/', signviews.custom_logout_view),
    path('', include('django.contrib.auth.urls')),
]

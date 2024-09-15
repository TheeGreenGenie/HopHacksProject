from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    age = models.CharField(max_length=5)
    risk = models.CharField(max_length=25)
    income = models.CharField(max_length=25)
    disposable_income = models.CharField(max_length=25)
    goal1 = models.CharField(max_length=60)
    goal2 = models.CharField(max_length=60)
    goal3 = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
from django.shortcuts import render
from django.http import HttpResponse
from .models import photos #importing photos model from models.py

#creating view 
def home(request):
    pic= photos.objects.all() #all objects of photos
    return render(request,"index.html", {'pics':pic})
  


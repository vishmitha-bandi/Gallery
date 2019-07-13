from django.shortcuts import render
from django.http import HttpResponse
from .models import photos
def home(request):
    pic= photos.objects.all()
    #con ={
     #   'pics':pic
    #}
    return render(request,"index.html", {'pics':pic})
    #return HttpResponse("hello")


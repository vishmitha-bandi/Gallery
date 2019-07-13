from django.contrib import admin
from django.urls import path
from  gallery.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home)
]
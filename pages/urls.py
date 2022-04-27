from django.urls import path
from . import views

urlpatterns = [
     #whenever below path is hit it will redirect to views.py file  
    path('',views.home, name='home'),
]

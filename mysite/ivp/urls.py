from .views import *
from django.urls import path

app_name = 'ivp'

urlpatterns = [
    path('', index, name='index'),
]

from django.urls import path
from .views import *

app_name='NavBar'

urlpatterns=[
    path('',logo,name='logo'),
    path('support/',support,name='support'),
    path('location/',locations,name='locations'),
    path('food/',food,name='food'),
]


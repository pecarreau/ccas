from django.urls import path
from . import  views
urlpatterns=[
    path('', views.CreatePersonne,name='nouvelle personne')
]
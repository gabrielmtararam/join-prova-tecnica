from django.conf.urls import  url
from django.urls import  include

from django.contrib import admin
from django.urls import path
from .views import questao1,questao1A,questao1B,questao1C

urlpatterns = [

    url(r'^$', questao1, name=''),
    url(r'A$', questao1A, name='A'),
    url(r'B$', questao1B, name='B'),
    url(r'C$', questao1C, name='C'),
]

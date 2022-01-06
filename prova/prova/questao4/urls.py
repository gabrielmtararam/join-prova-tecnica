from django.conf.urls import  url
from django.urls import  include

from django.contrib import admin
from django.urls import path
from .views import questao4

urlpatterns = [

    url(r'^$', questao4, name=''),

]

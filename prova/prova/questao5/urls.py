from django.conf.urls import  url
from django.urls import  include

from django.contrib import admin
from django.urls import path
from .views import questao5

urlpatterns = [

    url(r'^$', questao5, name='questao_5'),

]

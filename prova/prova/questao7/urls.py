from django.conf.urls import  url
from django.urls import  include

from django.contrib import admin
from django.urls import path
from .views import questao7,questao7Update,questa7DeleteMarker

urlpatterns = [

    url(r'^$', questao7, name='marker'),
    url(r'update$', questao7Update, name='update_marker'),
    url(r'delete-marker$', questa7DeleteMarker, name='delete_marker'),
]

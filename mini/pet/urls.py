from django.conf.urls import url
from . import main

urlpatterns = [
    url(r'^$', main.index, name='index'),        
]

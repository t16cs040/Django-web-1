'''
Created on 2018/10/17

@author: t16cs040
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
    ]
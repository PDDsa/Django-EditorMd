#coding:utf-8
import os

from django.conf.urls import url
from EditorMd import views

app_name = 'EditorMd'

urlpatterns = [
    url(r'^upload/$', views.upload, name='upload'),

]

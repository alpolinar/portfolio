from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^send_message/', send_message, name="send_message"),
]
from django.urls import path, include
from . import views

app_name = 'panel'

urlpatterns = [
    path('', views.index),
    path('settings', views.settings),
]
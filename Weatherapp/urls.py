from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexfile'),
    path('weathersystem', views.weathersystem, name='weathersystemfile'),
]


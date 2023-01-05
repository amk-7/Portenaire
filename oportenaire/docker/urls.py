from django.urls import path
from . import views

from django.db import models
app_name = "docker"


urlpatterns = [


	path('containers/', views.showContainers),
    path('images/', views.showImages),
    path('volumes/', views.showVolumes),



]
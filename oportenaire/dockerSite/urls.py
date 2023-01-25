from django.urls import path
from . import views

app_name = "dockerSite"

urlpatterns = [
    path('', views.index),
	path('containers/', views.showContainers, name="containers"),
    path('add_container/', views.addContainer, name="add_container"),
    path('images/', views.showImages, name="images"),
    path('volumes/', views.showVolumes, name="volumes"),
    path('run_image/', views.RunImage, name="run_image"),
    path('search_image_docker_hub/', views.searchImageDockerHub, name="search_image_docker_hub"),
]
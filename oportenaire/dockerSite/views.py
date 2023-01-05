from django.shortcuts import render
import dockerSite.docker_api as da
# Create your views here.
def showVolumes(request):
    volumes = [1,2,3]
    return render(request,"docker/volume.html",{"volumes":volumes})

def showContainers(request):
    containers = da.getContainers()
    print(containers)
    return render(request,"docker/containers.html",{"containers":containers})

def showImages(request):
    images = [1,2,3]
    return render(request,"docker/image.html",{"images":images})
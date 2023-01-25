from django.shortcuts import render, redirect
import dockerSite.docker_api as da

def index(request):
    return render(request, "dockerDesktop/index.html", context={})

def addContainer(request):
    return render(request, "dockerDesktop/add_container.html", context={})

def showVolumes(request):
    volumes = [1,2,3]
    return render(request,"dockerDesktop/volume.html",{"volumes":volumes})

def showContainers(request):
    containers = da.getContainers()
    #print(containers[0].attrs)
    return render(request,"dockerDesktop/containers.html",{"containers":containers})

def showImages(request):
    images = da.getImages()
    return render(request,"dockerDesktop/image.html",{"images":images})

def RunImage(request):
    da.runImage({})
    return redirect('/dockerSite/containers/')

def searchImageDockerHub(request):
    images = []
    if request.method == "POST":
        images = da.searchImage('debian')
    print(images[0])
    return render(request, "dockerHub/search_image.html", context={'images' : images})
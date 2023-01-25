import docker
import requests
#from . import exception as E
import exception as E

client = docker.from_env()

def getContainers():
    containers = client.containers.list(all=True)
    _containers = []
    for c in containers:
        _container = {}
        _container["name"] = c.name
        _container["state"] = c.attrs["State"]
        _container["image"] = "c.image"
        _container["created_at"] = c.attrs['Created']
        _container["ip_adresse"] = getKey(c.attrs['NetworkSettings']['Networks'])['IPAddress']
        _containers.append(_container)

    return _containers

def getImages():
    return client.images.list()

def pullImage(name: str):
    result = client.images.pull(name)
    return
        
def pushImage(image_id):
	pass

def findImageByNameAndTagg(image_name, tag_name):
	pass
	


def getVolumes():
    return client.volumes.list()

#::: Containers ::::::::::::::::::::::::::::::::::::
def runImage(context: dict) -> bool:
    result = None
    try :
        result = client.containers.run(image=context['image'], command=context['commande'][0], detach=context['detach'])
    except Exception as e:
        raise e
    print(result)
    return result == None

def removeContainer(container_id: str) -> bool:
    result = None
    try:
        container = findContainerIdByName(container_id)
        if container:
            result = container.remove()
    except Exception as e:
        raise e
    return result == None

def stopContainer(container_id):
    result = None
    try:
        container = findContainerIdByName(container_id)
        if container:
            result = container.stop()
    except Exception as e:
        raise e
    return result == None

def startContainair(container_id):
    result = None
    try:
        container = findContainerIdByName(container_id)
        if container:
            result = container.start()
    except Exception as e:
        raise e
    return result == None

def findContainerIdByName(containe_alpha):
    result = None
    try:
        containers = client.containers.list(all=True)
        for container in containers:
            if formatID(container.id) == containe_alpha:
                result = container
    except Exception as e:
        raise e
    return result

def formatID(id: str) -> str:
    return id[:12]

def getKey(dicti):
    for k in dicti :
        return dicti[k]

def searchImage(value):
    response = requests.get(f'https://hub.docker.com/api/content/v1/products/search?q={value}')
    if response.status_code == 200:
        data = response.json()
        if data['summaries'] == None:
            raise E.ImageFromDockerHubNotFound(f'L\'image {value} n\'a pas été trouvé.')

        return data['summaries']
    else:
        raise E.ImageFromDockerHubNotFound(f'Erreur de connection code {response.status_code}')

#print(getImages()[0].attrs)
#print(searchImage('debian'))
#getContainers()
#runImage({"image": "alpine", "commande":["echo 'hello world'"], "detach" : False})
#removeContainer("729d418b3b29")
startContainair("4ea683d1e24f")

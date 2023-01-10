import docker
import requests

client = docker.from_env()


def getContainers():
    return client.containers.list()

def getImages():
    return client.images.list()

def getVolumes():
    return client.volumes.list()


#print(getImages()[0].attrs)

def researchImage(system):
    nom = 'ubuntu'
    response = requests.get('https://hub.docker.com/api/content/v1/products/search?q='+nom)
    # Vérifier que la réponse est correcte
    if response.status_code == 200:
        # Charger les données JSON de la réponse
        data = response.json()
        # Afficher la liste des images
        listImage={}
        for image in data['summaries']:
            listImage =image['name']
            #print(image['name'])
            print(listImage)

        #print(data["summaries"])
        return listImage
    else:
        # Afficher le message d'erreur
        print('Erreur lors de la récupération des données code : ', response.status_code)
researchImage('')
"""for img in getImages():
    print(img.attrs)"""
"""import docker
client_host = docker.DockerClient()

images = client_host.images.list()
print(images)"""

import requests

# Envoyer une requête GET à l'API de Docker Hub pour récupérer la liste des images
#response = requests.get('https://hub.docker.com/v2/search?q=nginx')
"""data = {
	"username" : "",
	"password" : ""
}
response = requests.get('https://hub.docker.com/v2/users/login', json=data)
# Vérifier que la réponse est correcte
if response.status_code == 200:
  # Charger les données JSON de la réponse
  data = response.json()
  # Récupérer la liste des images de la réponse
  tk = data['token']
  # Afficher la liste des images
  print(tk)
else:
  # Afficher le message d'erreur
  print('Erreur lors de la récupération des données')"""


response = requests.get('https://hub.docker.com/search?q=nginx')
# Vérifier que la réponse est correcte
if response.status_code == 200:
  # Charger les données JSON de la réponse
  data = response
  # Afficher la liste des images
  print(data)
else:
  # Afficher le message d'erreur
  print('Erreur lors de la récupération des données code : ', response.status_code)

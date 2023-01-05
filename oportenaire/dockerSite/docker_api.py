import docker 

client = docker.from_env()


def getContainers():
    return client.containers.list()



class ImageFromDockerHubNotFound(Exception):
    def __init__(self, _message: str) -> None:
        self.message = _message
        super().__init__(self.message)
    def __str__(self):
        return self.message
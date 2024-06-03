class MediaType:
    def __init__(self, id, name) -> None:
        self.id:    int = id
        self.name:  str = name

    def __str__(self):
        return f': {self.name}'

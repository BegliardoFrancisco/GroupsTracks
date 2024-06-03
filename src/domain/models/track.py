from src.domain.models.media_type import MediaType
from src.domain.models.genre import Genre


class Track:
    def __init__(self, id: int, name: str, composer: str, miliseconds: int,
                 quanty_bytes: int, unitprice: float, genre: Genre | None = None,
                 mediatype: MediaType | None = None):
        self.id: int = id
        self.name: str = name
        self.composer: str = composer
        self.miliseconds: int = miliseconds
        self.bytes: int = quanty_bytes
        self.unitprice: float = unitprice
        self.mediatype: MediaType = mediatype
        self.genre: Genre = genre

    def __str__(self):
        return ('{' +
                    (f' id: {self.id},\n'
                       f'  name: {self.name},\n'
                       f'  composer: {self.composer},\n'
                       f'  miliseconds: {self.miliseconds},\n'
                       f'  bytes: {self.miliseconds}\n'
                       f'  unitprice: {self.unitprice},\n'
                       f'  mediatype: {self.mediatype},\n'
                       f'  genre: {self.genre},\n') +
                '}')

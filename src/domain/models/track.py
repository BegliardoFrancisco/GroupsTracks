from src.domain.models.media_type import MediaType
from typing import List
from src.domain.models.genre import Genre


class Track:
    def __int__(self, id: int, name: str, composer: str, miliseconds: int,
                quanty_bytes: int, unitprice: float, genre: Genre | None = None,
                mediatype: List[MediaType] | None = None):
        self.id: int = id
        self.name: str = name
        self.composer: str = composer
        self.miliseconds: int = miliseconds
        self.bytes: int = quanty_bytes
        self.unitprice: float = unitprice
        self.mediatype: List[MediaType] = mediatype
        self.genre: Genre = genre

    def add_mediatype(self, media):
        self.mediatype.append(media)

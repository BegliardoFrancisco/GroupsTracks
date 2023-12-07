from media_type import MediaType
from typing import List


class Track:
    def __int__(self, id: int, name: str, composer: str, miliseconds: int,
                quanty_bytes: int, unitprice: float, mediatype: List[MediaType]):
        self.id: int = id
        self.name: str = name
        self.composer: str = composer
        self.miliseconds: int = miliseconds
        self.bytes: int = quanty_bytes
        self.unitprice: float = unitprice
        self.mediatype: List[MediaType] = mediatype

    def add_mediatype(self, media):
        self.mediatype.append(media)

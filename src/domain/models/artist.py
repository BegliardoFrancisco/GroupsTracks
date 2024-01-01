from src.domain.models.album import Album
from typing import List
import asyncio


class Artist:
    def __init__(self, id, name, albums: List[Album] = None) -> None:
        self.id: int = id
        self.name: str = name
        self.albums: List[Album] = albums if albums is not None else []

    async def add_album(self, album: Album) -> None:
        if isinstance(album, Album):
            self.albums.append(album)
        else:
            raise TypeError(f"the album argument no is type Album class:{__class__} in {__name__} {__file__}")

    async def add_albums(self, tracks: List[Album]):

        add_track_task = [await self.add_album(track) for track in tracks]
        await asyncio.gather(**add_track_task)

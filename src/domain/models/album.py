import asyncio

from src.domain.models.track import Track
from typing import List


class Album:

    def __init__(self, id, title, tracks: List[Track] = None) -> None:
        self.id: int = id
        self.title: str = title
        self.tracks: List[Track] = tracks if tracks is not None else []

    async def add_track(self, track: Track):
        if isinstance(track, Track):
            self.tracks.append(track)
        else:
            raise TypeError(f"The track argument not is type Track is type:{type(track)} class:{__class__} in {__name__} {__file__}")

    async def add_tracks(self, tracks: List[Track]):

        add_track_task = [await self.add_track(track) for track in tracks]
        await asyncio.gather(*add_track_task)

    def __str__(self):
        return f'id: {self.id} title: {self.title}'
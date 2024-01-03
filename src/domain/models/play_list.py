import asyncio
from typing import List
from src.domain.models.track import Track


class PlayList:

    def __init__(self, id: int, name: str, tracks: List[Track] = None):
        self.id: int = id
        self.name: str = name
        self.tracks: List[Track] = tracks if tracks is not None else []

    async def add_track(self, track: Track) -> None:
        if isinstance(track, Track):
            self.tracks.append(track)
        else:
            raise TypeError(f"the track argument no is type Track class:{__class__} in {__name__} {__file__}")

    async def add_tracks(self, tracks: List[Track]):
        if isinstance(tracks, List):
            await asyncio.gather(*[self.add_track(track) for track in tracks])
        else:
            raise TypeError(f"the track argument no is type List class:{__class__} in {__name__} {__file__}")

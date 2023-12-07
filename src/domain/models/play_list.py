from typing import List
from src.domain.models.track import Track


class PlayList:

    def __int__(self, id: int, name: str, tracks: List[Track] = None):
        self.id: int = id
        self.name: str = name
        self.tracks: List[Track] = tracks if tracks is not None else []

    def add_track(self, track: Track) -> None:
        if isinstance(track, Track):
            self.tracks.append(track)
        else:
            raise TypeError(f"the track argument no is type Track class:{__class__} in {__name__} {__file__}")

from src.domain.models.track import Track
from typing import List


class Album:

    def __int__(self, id, title, tracks: List[Track] = None) -> None:
        self.id: int = id
        self.title: str = title
        self.tracks: List[Track] = tracks if tracks is not None else []

    def add_track(self, track: Track):
        if isinstance(track, Track):
            self.tracks.append(track)
        else:
            raise TypeError(f"the track argument no is type Track class:{__class__} in {__name__} {__file__}")

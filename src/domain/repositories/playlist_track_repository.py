from abc import ABCMeta, abstractmethod
from typing import List
from ..models.track import Track


class TracksInPlaylistRepository(ABCMeta):
    @abstractmethod
    def get_tracks_from_playlist(cls, playlist_id: int) -> List[Track]:
        raise NotImplementedError('NotImplementedError: '
                                  f'get_tracks_from_playlist method in {__class__}')

from abc import ABC, abstractmethod
from typing import List
from src.domain.repositories.track_repository import TrackRepository

class TracksInPlaylistRepository(ABC):

    @abstractmethod
    async def add_track_from_playlist(cls, track_id: int, playlist_id: int) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'add_track_from_playlist method in {__class__}')

    @abstractmethod
    async def add_tracks_from_playlist(cls, tracks_id: List[int], playlist_id: int) ->None:
        raise NotImplementedError('NotImplementedError: '
                                  f'add_tracks_from_playlist method in {__class__}')

    @abstractmethod
    async def delete_track_from_playlist(cls, track_id: int, playlist_id: int) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'delete_track_from_playlist method in {__class__}')
    
    @abstractmethod
    async def delete_tracks_from_playlist(cls, tracks_id: List[int], playlist_id: int) -> None:
        raise NotImplementedError('NotImplementedError: '
                                f'delete_tracks_from_playlist method in {__class__}')
    
    

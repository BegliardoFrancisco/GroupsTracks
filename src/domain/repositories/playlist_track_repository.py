from abc import ABC, abstractmethod
from typing import List
from .genres_repository import GenreRepositories
from .media_type_repository import MediaTypeRepositories
from ..models.track import Track


class TracksInPlaylistRepository(ABC):

    def __init__(self, media_type_repository: MediaTypeRepositories, genre_repository: GenreRepositories):
        self.media_type_repository = media_type_repository
        self.genre_repository = genre_repository

    @abstractmethod
    async def get_track_from_playlist(cls, track_id: int, playlist_id: int) -> List[Track]:
        raise NotImplementedError('NotImplementedError: '
                                  f'get_track_from_playlist method in {__class__}')

    @abstractmethod
    async def add_track_from_playlist(cls, track_id: int, playlist_id: int) -> List[Track]:
        raise NotImplementedError('NotImplementedError: '
                                  f'add_track_from_playlist method in {__class__}')

    @abstractmethod
    async def add_tracks_from_playlist(cls, tracks_id: List[int], playlist_id: int) -> List[Track]:
        raise NotImplementedError('NotImplementedError: '
                                  f'add_tracks_from_playlist method in {__class__}')

    @abstractmethod
    async def delete_track_from_playlist(cls, track_id: int, playlist_id: int) -> List[Track]:
        raise NotImplementedError('NotImplementedError: '
                                  f'delete_track_from_playlist method in {__class__}')

    @abstractmethod
    async def get_tracks_from_playlist(cls, playlist_id: int) -> List[Track]:
        raise NotImplementedError('NotImplementedError: '
                                  f'get_tracks_from_playlist method in {__class__}')

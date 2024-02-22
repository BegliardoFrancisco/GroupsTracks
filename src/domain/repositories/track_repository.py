from abc import ABC, abstractmethod
from src.domain.models.track import Track
from typing import List

from src.domain.repositories.genres_repository import GenreRepositories
from src.domain.repositories.media_type_repository import MediaTypeRepositories


class TrackRepository(ABC):

    def __init__(self, media_type_repository: MediaTypeRepositories, genre_repository: GenreRepositories):
        self.media_type_repository = media_type_repository
        self.genre_repository = genre_repository

    @abstractmethod
    async def get_all_tracks(cls) -> List[Track]:
        raise NotImplementedError(f'NotImplementedError: '
                                  f'get_all_tracks method in {__class__}')

    @abstractmethod
    async def get_track_by_id(cls, id: int) -> Track:
        raise NotImplementedError('NotImplementedError: '
                                  f'get_track_by_id method in {__class__}')

    @abstractmethod
    async def add_track(cls, track: Track) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'add_track method in {__class__}')

    @abstractmethod
    async def delete_track(cls, track: Track) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'delete_track method in {__class__}')

    @abstractmethod
    async def update_track(cls, track: Track) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'update_track method in {__class__}')

    @abstractmethod
    async def get_tracks_from_album(cls, album_id: int) -> List[Track]:
        raise NotImplementedError('NotImplementedError: '
                                  f'et_tracks_from_album method in {__class__}')

    @abstractmethod
    async def get_tracks_from_playlist(cls, playlist_id: int) -> List[Track]:
        raise NotImplementedError('NotImplementedError: '
                                  f'et_tracks_from_playlist method in {__class__}')

    @abstractmethod
    async def check_exist_tracks(cls, tracks_ids: List[int]) -> bool:
        raise NotImplementedError('NotImplementedError: '
                                  f'check_exist_tracks method in {__class__}')
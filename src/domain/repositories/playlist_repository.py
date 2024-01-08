from abc import ABC, abstractmethod
from typing import List
from src.domain.repositories.genres_repository import GenreRepositories
from src.domain.repositories.media_type_repository import MediaTypeRepositories
from src.domain.models.play_list import PlayList
from src.domain.repositories.track_repository import TrackRepository


class PlayListRepositories(ABC):

    def __init__(self,genre_repository: GenreRepositories , media_type_repository: MediaTypeRepositories):

        self.genre_repository: GenreRepositories = genre_repository
        self.media_type_repository: MediaTypeRepositories = media_type_repository

    @abstractmethod
    async def get_all_playlist(cls) -> List[PlayList]:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_all_playlist no implemented method in class: {__class__}")

    @abstractmethod
    async def get_playlist_id(cls, id: int) -> PlayList:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_playlist_id no implemented method in class: {__class__}")

    @abstractmethod
    async def add_playlist(cls, playlist: PlayList) -> None:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"add_playlist no implemented method in class: {__class__}")

    @abstractmethod
    async def delete_playlist(cls, playlist_id: int) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'delete_playlist method in {__class__}')

    @abstractmethod
    async def update_playlist(cls, playlist: PlayList) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'update_playlist method in {__class__}')

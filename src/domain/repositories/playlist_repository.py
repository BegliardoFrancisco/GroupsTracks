from abc import ABC, abstractmethod
from typing import List
from src.domain.models.play_list import PlayList
from src.domain.repositories.playlist_track_repository import TracksInPlaylistRepository


class PlayListRepositories(ABC):

    def __init__(self, track_playlist_repository: TracksInPlaylistRepository):
        self.track_playlist_repository: TracksInPlaylistRepository = track_playlist_repository

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

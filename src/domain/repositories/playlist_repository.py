from abc import ABCMeta, abstractmethod
from typing import List
from src.domain.models.play_list import PlayList


class PlayListRepositories(ABCMeta):

    @abstractmethod
    def get_all_playlist(cls) -> List[PlayList]:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_all_playlist no implemented method in class: {__class__}")

    @abstractmethod
    def get_playlist_id(cls, id: int) -> PlayList:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_playlist_id no implemented method in class: {__class__}")

    @abstractmethod
    def add_playlist(cls, playlist: PlayList) -> None:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"add_playlist no implemented method in class: {__class__}")

    @abstractmethod
    def delete_playlist(cls, playlist: PlayList) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'delete_playlist method in {__class__}')

    @abstractmethod
    def update_playlist(cls, playlist: PlayList) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'update_playlist method in {__class__}')

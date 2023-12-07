from abc import ABCMeta, abstractmethod
from typing import List
from src.domain.models.album import Album


class AlbumRepositories(ABCMeta):

    @abstractmethod
    def get_all_album(cls) -> List[Album]:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_all_album no implemented method in class: {__class__}")

    @abstractmethod
    def get_albums_from_artist(cls, artist_id: int) -> List[Album]:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_all_album no implemented method in class: {__class__}")

    @abstractmethod
    def get_album_id(cls, id: int) -> Album:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_album_id no implemented method in class: {__class__}")

    @abstractmethod
    def add_album(cls, album: Album) -> None:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"add_album no implemented method in class: {__class__}")
    
    @abstractmethod
    def delete_album(cls, album: Album) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'delete_album method in {__class__}')

    @abstractmethod
    def update_album(cls, album: Album) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'update_album method in {__class__}')

from abc import ABC, abstractmethod
from typing import List
from src.domain.models.album import Album


class AlbumRepositories(ABC):

    @abstractmethod
    async def get_all_album(self) -> List[Album]:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_all_album no implemented method in class: {__class__}")

    @abstractmethod
    async def get_albums_from_artist(self, artist_id: int) -> List[Album]:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_all_album no implemented method in class: {__class__}")

    @abstractmethod
    async def get_album_id(self, id: int) -> Album:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_album_id no implemented method in class: {__class__}")

    @abstractmethod
    async def add_album(self, album: Album, artist_id: int) -> None:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"add_album no implemented method in class: {__class__}")
    
    @abstractmethod
    async def delete_album(self, album_id: int) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'delete_album method in {__class__}')

    @abstractmethod
    async def update_album(self, album: Album, artist_id: int) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'update_album method in {__class__}')


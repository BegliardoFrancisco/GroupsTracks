from abc import ABC, abstractmethod
from typing import List
from src.domain.models.artist import Artist


class ArtistRepositories(ABC):

    @abstractmethod
    async def get_all_artist(cls) -> List[Artist]:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_all_artist no implemented method in class: {__class__}")

    @abstractmethod
    async def get_artist_id(cls, id: int) -> Artist:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_artist_id no implemented method in class: {__class__}")

    @abstractmethod
    async def add_artist(cls, artist: Artist) -> None:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"add_artist no implemented method in class: {__class__}")

    @abstractmethod
    async def delete_artist(cls, artist_id: int) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'delete_artist method in {__class__}')

    @abstractmethod
    async def update_artist(cls, artist: Artist) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'update_artist method in {__class__}')

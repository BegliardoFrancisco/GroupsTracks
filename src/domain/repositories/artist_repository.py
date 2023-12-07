from abc import ABCMeta, abstractmethod
from typing import List
from src.domain.models.artist import Artist


class ArtistRepositories(ABCMeta):

    @abstractmethod
    def get_all_artist(cls) -> List[Artist]:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_all_artist no implemented method in class: {__class__}")

    @abstractmethod
    def get_artist_id(cls, id: int) -> Artist:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_artist_id no implemented method in class: {__class__}")

    @abstractmethod
    def add_artist(cls, artist: Artist) -> None:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"add_artist no implemented method in class: {__class__}")

    @abstractmethod
    def delete_artist(cls, artist: Artist) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'delete_artist method in {__class__}')

    @abstractmethod
    def update_artist(cls, artist: Artist) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'update_artist method in {__class__}')

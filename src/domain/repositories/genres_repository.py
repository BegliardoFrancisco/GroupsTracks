from abc import ABCMeta, abstractmethod
from typing import List
from src.domain.models.genre import Genres


class GenresRepositories(ABCMeta):

    @abstractmethod
    def get_all_genres(cls) -> List[Genres]:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_all_genres no implemented method in class: {__class__}")

    @abstractmethod
    def get_genres_id(cls, id: int) -> Genres:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_genres_id no implemented method in class: {__class__}")

    @abstractmethod
    def add_genres(cls, genres: Genres) -> None:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"add_genres no implemented method in class: {__class__}")

    @abstractmethod
    def delete_genres(cls, genres: Genres) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'delete_genres method in {__class__}')

    @abstractmethod
    def update_genres(cls, genres: Genres) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'update_genres method in {__class__}')

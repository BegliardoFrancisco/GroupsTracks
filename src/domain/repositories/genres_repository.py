from abc import ABC, abstractmethod
from typing import List
from src.domain.models.genre import Genre


class GenreRepositories(ABC):

    @abstractmethod
    async def get_all_genres(self) -> List[Genre]:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_all_genres no implemented method in class: {__class__}")

    @abstractmethod
    async def get_genres_id(self, id: int) -> Genre:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_genres_id no implemented method in class: {__class__}")

    @abstractmethod
    async def add_genres(self, genres: Genre) -> None:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"add_genres no implemented method in class: {__class__}")

    @abstractmethod
    async def delete_genres(self, id: int) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'delete_genres method in {__class__}')


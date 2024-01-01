from abc import ABC, abstractmethod
from typing import List
from src.domain.models.media_type import MediaType


class MediaTypeRepositories(ABC):

    @abstractmethod
    async def get_all_media_type(cls) -> List[MediaType]:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_all_media_type no implemented method in class: {__class__}")

    @abstractmethod
    async def get_media_type_id(cls, id: int) -> MediaType:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_media_type_id no implemented method in class: {__class__}")

    @abstractmethod
    async def add_media_type(cls, media_type: MediaType) -> None:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"add_media_type no implemented method in class: {__class__}")

    @abstractmethod
    async def delete_media_type(cls, media_type: MediaType) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'delete_media_type method in {__class__}')

    @abstractmethod
    async def update_media_type(cls, media_type: MediaType) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'update_media_type method in {__class__}')

    @abstractmethod
    async def get_media_type_from_track(self, track_id: int) -> MediaType:
        raise NotImplementedError('NotImplementedError: '
                                  f'get_media_type_from_track method in {__class__}')
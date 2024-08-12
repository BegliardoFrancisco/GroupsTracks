from typing import List
from src.application.requests.artist_request import NewArtistRequest, ArtistRequestUpdate
from src.domain.repositories.artist_repository import ArtistRepositories
from src.application.responses.artist_responses import ArtistResponses
from abc import ABC, abstractmethod


class ArtistService(ABC):

    @abstractmethod
    def __init__(self, artist_repositories: ArtistRepositories):
        self.artist_repostory = artist_repositories

    @abstractmethod
    async def get_all_artist(self) -> List[ArtistResponses]:
        raise NotImplementedError('not implemented method get_all_artist from ArtistService')

    @abstractmethod
    async def get_artist_id(self, artist_id: int) -> ArtistResponses:
        raise NotImplementedError('not implemented method get_artist_id from ArtistService')

    @abstractmethod
    async def add_artist(self, artist: NewArtistRequest):
        raise NotImplementedError('not implemented method get_artist_id from ArtistService')

    @abstractmethod
    async def update_artist(self, artist: ArtistRequestUpdate):
        raise NotImplementedError('not implemented method update_artist from ArtistService')

    @abstractmethod
    async def delete_artist(self, artist_id: int):
        raise NotImplementedError('not implemented method delete_artist from ArtistService')

from typing import List

from src.domain.services.artist_service import ArtistService
from src.domain.repositories.artist_repository import ArtistRepositories
from src.application.responses.artist_responses import SimpleArtistResponses, ArtistResponses
from src.application.requests.artist_request import ArtistRequest
from src.application.responses.artist_responses import ConverterArtist


class ArtistServiceImpl(ArtistService):

    def __init__(self, artist_repo: ArtistRepositories, ):
        self.artist_repository = artist_repo

    async def get_all_artist(self) -> List[SimpleArtistResponses]:
        try:
            artists = await self.artist_repository.get_all_artist()

            response: List[SimpleArtistResponses] = [
                await ConverterArtist.to_simple_response(artist)
                for artist in artists
            ]
            return response
        except Exception as e:
            raise e

    async def get_artist_id(self, artist_id: int) -> ArtistResponses:
        try:
            artist = await self.artist_repository.get_artist_id(artist_id)
            response: ArtistResponses = await ConverterArtist.to_response(artist)

            return response

        except Exception as e:
            raise e

    async def add_artist(self, artist: ArtistRequest):
        pass

    async def update_artist(self, artist: ArtistRequest):
        pass

    async def delete_artist(self, artist_id: int):
        pass

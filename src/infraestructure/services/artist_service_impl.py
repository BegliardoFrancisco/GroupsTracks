from typing import List
from src.domain.models.artist import Artist
from src.domain.services.artist_service import ArtistService
from src.domain.repositories.artist_repository import ArtistRepositories
from src.application.responses.artist_responses import SimpleArtistResponses
from src.application.requests.artist_request import NewArtistRequest, ArtistRequestUpdate
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

    async def get_artist_id(self, artist_id: int) -> SimpleArtistResponses:
        try:
            artist = await self.artist_repository.get_artist_id(artist_id)
            response: SimpleArtistResponses = await ConverterArtist.to_simple_response(artist)

            return response

        except Exception as e:
            raise e

    async def add_artist(self, artist: NewArtistRequest):

        new_artist = Artist(artist.name, None)

        try:

            await self.artist_repository.add_artist(new_artist)
        except Exception as e:
            raise e

    async def update_artist(self, artist: ArtistRequestUpdate):
        try:

            if artist.if_with_id():
                raise ValueError('Artist must have an ID to allow an update')

            artist_select = Artist(artist.id, artist.name, None)
            await self.artist_repository.update_artist(artist_select)

        except Exception as e:
            raise e

    async def delete_artist(self, artist_id: int):

        try:

            if artist_id is None:
                raise ValueError('id is required to delete the user')

            await self.artist_repository.delete_artist(artist_id)

        except Exception as e:
            raise e

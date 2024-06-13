from pydantic import BaseModel
from typing import List
from src.application.responses.album_responses import AlbumResponses, ConverterAlbum
from src.domain.models.artist import Artist


class ArtistResponses(BaseModel):
    id: int
    name: str
    albums: List[AlbumResponses]


class ConverterArtist:
    @staticmethod
    async def to_response(artist: Artist) -> ArtistResponses:
        albums_response: List[AlbumResponses] = [
            await ConverterAlbum.to_response(album)
            for album in artist.albums
        ]
        return ArtistResponses(
            id=artist.id,
            name=artist.name,
            albums=albums_response
        )

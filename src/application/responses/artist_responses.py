from pydantic import BaseModel
from typing import List
from src.application.responses.album_responses import AlbumResponses, ConverterAlbum
from src.domain.models.artist import Artist


class ArtistResponses(BaseModel):
    id: int
    name: str
    albums: List[AlbumResponses]


class SimpleArtistResponses(BaseModel):
    id: int
    name: str


class ConverterArtist:
    @staticmethod
    async def to_response(artist: Artist) -> 'ArtistResponses':

        if not artist.albums:
            albums_response = []
        albums_response: List[AlbumResponses] = [
            await ConverterAlbum.to_response(album)
            for album in artist.albums
        ]
        return ArtistResponses(
            id=artist.id,
            name=artist.name,
            albums=albums_response
        )

    @staticmethod
    async def to_simple_response(artist: Artist) -> 'SimpleArtistResponses':
        return SimpleArtistResponses(
            id=artist.id,
            name=artist.name,
        )
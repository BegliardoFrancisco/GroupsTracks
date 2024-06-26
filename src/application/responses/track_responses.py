from pydantic import BaseModel
from typing import Optional

from src.domain.models.track import Track
from src.application.responses.genre_responses import GenreResponses, ConverterGenre
from src.application.responses.mediatype_responses import MediaTypeResponses, ConverterMediaType


class TrackResponses(BaseModel):
    id: int
    name: str
    composer: Optional[str]
    miliseconds: int
    bytes: int
    unitprice: float
    mediatype: MediaTypeResponses
    genre: GenreResponses


class ConverterTrack:
    @staticmethod
    async def to_response(track: Track) -> TrackResponses:

        if not track.mediatype:
            media_type = None
        if not track.genre:
            genre = None
        media_type: MediaTypeResponses = await ConverterMediaType.to_response(track.mediatype)
        genre: GenreResponses = await ConverterGenre.to_response(track.genre)

        return TrackResponses(
            id=track.id,
            name=track.name,
            composer=track.composer,
            miliseconds=track.miliseconds,
            bytes=track.bytes,
            unitprice=track.unitprice,
            mediatype=media_type,
            genre=genre
        )

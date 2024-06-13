from typing import List
from pydantic import BaseModel
from src.application.responses.track_responses import TrackResponses, ConverterTrack
from src.domain.models.album import Album


class AlbumResponses(BaseModel):
    id: int
    title: str
    tracks: List[TrackResponses]


class ConverterAlbum:
    @staticmethod
    async def to_response(album: Album) -> 'AlbumResponses':
        tracks_responses: List[TrackResponses] = [
            await ConverterTrack.to_response(track)
            for track in album.tracks
        ]

        return AlbumResponses(
            id=album.id,
            title=album.title,
            tracks=tracks_responses
        )

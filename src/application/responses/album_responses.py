from typing import List, Optional
from pydantic import BaseModel
from src.application.responses.track_responses import TrackResponses, ConverterTrack
from src.domain.models.album import Album


class AlbumResponses(BaseModel):
    id: int
    title: str
    tracks: Optional[List[TrackResponses]]


class SimpleAlbumResponses(BaseModel):
    id: int
    title: str


class ConverterAlbum:
    @staticmethod
    async def to_response(album: Album) -> 'AlbumResponses':
        tracks_responses = []
        if album.tracks and len(album.tracks) >= 0:
            tracks_responses: List[TrackResponses] = [
                await ConverterTrack.to_response(track)
                for track in album.tracks
            ]

        return AlbumResponses(
            id=album.id,
            title=album.title,
            tracks=tracks_responses
        )

    @staticmethod
    async def to_simple_response(album: Album) -> 'SimpleAlbumResponses':
        return SimpleAlbumResponses(
            id=album.id,
            title=album.title
        )

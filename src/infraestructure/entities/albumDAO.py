from typing import List

from src.domain.models.album import Album
from src.domain.models.track import Track
from src.infraestructure.entities.trackDAO import TrackDAO
from src.infraestructure.entities.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class AlbumDAO(Base):
    __tablename__: str = 'albums'
    AlbumId: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    ArtistId: Mapped[int] = mapped_column(ForeignKey('artists.ArtistId'))
    tracks = relationship('TrackDAO', backref='tracks', lazy='selectin')

    async def from_domain(self, ) -> Album:
        tracks_from_albums: List[Track] = [
            await track.from_domain()
            for track in self.tracks
        ]
        return Album(
            id=self.AlbumId,
            title=self.title,
            tracks=tracks_from_albums
        )

    @staticmethod
    async def from_dto(album: Album, artist_id: int) -> 'AlbumDAO':
        return AlbumDAO(AlbumId=album.id, title=album.title, ArtistId=artist_id)

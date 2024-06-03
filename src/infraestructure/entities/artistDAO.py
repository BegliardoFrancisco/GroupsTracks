from typing import List
from src.domain.models.album import Album
from src.domain.models.artist import Artist
from src.domain.repositories.album_repository import AlbumRepositories
from src.infraestructure.entities.base import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column


class ArtistDAO(Base):
    __tablename__ = 'artists'
    ArtistId: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str]
    albums = relationship('AlbumDAO', backref='albums', lazy='selectin')

    async def from_domain(self,) -> Artist:

        albums_from_artist = [
            await album.from_domain()
            for album in self.albums
        ]
        return Artist(
            id=self.ArtistId,
            name=self.Name,
            albums=albums_from_artist
        )

    @staticmethod
    async def from_dto(artist: Artist) -> 'ArtistDAO':

        return ArtistDAO(
            ArtistId=artist.id,
            Name=artist.name
        )

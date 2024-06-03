from src.infraestructure.entities.base import Base
from src.domain.repositories.genres_repository import GenreRepositories
from src.infraestructure.entities.genresDAO import GenresDAO
from src.infraestructure.entities.media_typesDAO import MediaTypeDAO
from src.domain.repositories.media_type_repository import MediaTypeRepositories
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from src.domain.models.track import Track


class TrackDAO(Base):
    __tablename__ = "tracks"
    TrackId: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str]
    Composer: Mapped[str]
    Milliseconds: Mapped[int]
    Bytes: Mapped[int]
    UnitPrice: Mapped[float]
    AlbumId: Mapped[int] = mapped_column(ForeignKey("albums.AlbumId"))
    MediaTypeId: Mapped[int] = mapped_column(ForeignKey("media_types.MediaTypeId"))
    media_type: Mapped['MediaTypeDAO'] = relationship(lazy='selectin')
    GenreId: Mapped[int] = mapped_column(ForeignKey("genres.GenreId"))
    genre: Mapped['GenresDAO'] = relationship(lazy='selectin')

    async def from_domain(self, ) -> Track:
        try:
            genre = await self.genre.from_domain()
            mediatype = await self.media_type.from_domain()
            return Track(id=self.TrackId,
                     name=self.Name,
                     composer=self.Composer,
                     miliseconds=self.Milliseconds,
                     quanty_bytes=self.Bytes,
                     unitprice=self.UnitPrice,
                     genre=genre,
                     mediatype=mediatype)
        except Exception as e:
            print(f'{e}')
            raise e
    @staticmethod
    async def from_dto(track: Track) -> 'TrackDAO':
        return TrackDAO(
            TrackId=track.id,
            Name=track.name,
            Composer=track.composer,
            Milliseconds=track.miliseconds,
            Bytes=track.bytes,
            UnitPrice=track.unitprice,
            GenreId=track.genre.id,
            MediaTypeId=track.mediatype.id
        )


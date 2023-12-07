from src.infraestructure.entities.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


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
    GenreId: Mapped[int] = mapped_column(ForeignKey("genres.GenresId"))
    
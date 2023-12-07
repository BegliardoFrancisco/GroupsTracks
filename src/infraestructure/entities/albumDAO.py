from src.infraestructure.entities.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class AlbumDAO(Base):
    __tablename__: str = 'albums'
    AlbumId: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    ArtistId: Mapped[int] = mapped_column(ForeignKey('artists.ArtistId'))
    
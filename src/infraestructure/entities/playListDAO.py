from src.infraestructure.entities.base import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class PlayListDAO(Base):
    __tablename__: str = "playlists"
    PlaylistId: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str]
    
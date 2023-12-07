from src.infraestructure.entities.base import Base

from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import mapped_column


class PlayList_TrackDAO(Base):
    __tablename__ = "playlist_track"
    PlaylistId: Mapped[int] = mapped_column(ForeignKey("playlists.PlaylistId"))
    TrackId: Mapped[int]= mapped_column(ForeignKey("tracks.TrackId"))
    
    __table_args__ = (
        PrimaryKeyConstraint(PlaylistId, TrackId),
    )
    
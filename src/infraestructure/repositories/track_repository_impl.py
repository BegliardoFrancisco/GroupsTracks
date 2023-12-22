from src.domain.repositories.track_repository import TrackRepository
from src.domain.models.track import Track
from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories import engine


class TrackRepositoryImpl(TrackRepository):

    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_all_tracks(self) -> List[Track]:
        pass

    def get_track_by_id(self, id: int) -> Track:
        pass

    def add_track(self, track: Track) -> None:
        pass

    def delete_track(self, track: Track) -> None:
        pass

    def update_track(self, track: Track) -> None:
        pass

    def get_tracks_from_album(self, album_id: int) -> List[Track]:
        pass

from src.domain.repositories.track_repository import TrackRepository
from src.domain.repositories.playlist_track_repository import TracksInPlaylistRepository
from src.infraestructure.entities.trackDAO import TrackDAO
from src.infraestructure.entities.playListDAO import PlayListDAO
from src.infraestructure.entities.playlist_trackDAO import PlayList_TrackDAO
from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from . import engine
from sqlalchemy import delete



class TracksInPlaylistRepositoryImpl(TracksInPlaylistRepository):

    def __init__(self):
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
           
    async def add_track_from_playlist(self, track_id: int, playlist_id: int) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        PlayList_TrackDAO(
                           PlaylistId= playlist_id,
                           TrackId= track_id
                        )
                    ])
        except Exception as e:
            print(f"Error in add_track_from_playlist: {str(e)}")
            raise e

    async def add_tracks_from_playlist(self, tracks_id: List[int], playlist_id: int) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        PlayList_TrackDAO(
                           PlaylistId= playlist_id,
                           TrackId= track_id
                        )
                        for track_id in tracks_id
                    ])
        except Exception as e:
            print(f"Error in add_tracks_from_playlist: {str(e)}")
            raise e

    async def delete_track_from_playlist(self, track_id: int, playlist_id: int) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    await session.execute(
                        delete(PlayList_TrackDAO).where(PlayList_TrackDAO.PlaylistId == playlist_id and PlayList_TrackDAO.TrackId == track_id)
                    )
        except Exception as e:
            print(f"delete_track_from_playlist: {str(e)}")
            raise e
    
    async def delete_tracks_from_playlist(self, tracks_id: List[int], playlist_id: int) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    await session.execute(
                        delete(PlayList_TrackDAO).where(PlayList_TrackDAO.PlaylistId == playlist_id and PlayList_TrackDAO.TrackId in tracks_id)
                    )
        except Exception as e:
            print(f"delete_tracks_from_playlist: {str(e)}")
            raise e
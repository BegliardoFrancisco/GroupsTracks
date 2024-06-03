import asyncio

from src.domain.repositories.genres_repository import GenreRepositories
from src.domain.repositories.media_type_repository import MediaTypeRepositories
from src.domain.repositories.track_repository import TrackRepository
from src.domain.models.track import Track
from src.infraestructure.entities.trackDAO import TrackDAO
from typing import List
from sqlalchemy.orm import sessionmaker, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories import engine
from sqlalchemy import select, delete, update
from src.infraestructure.entities.playlist_trackDAO import PlayList_TrackDAO


class TrackRepositoryImpl(TrackRepository):

    def __init__(self,):
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_all_tracks(self) -> List[Track]:
        try:
            async with self.async_session() as session:
                query = select(TrackDAO)

                tracks = (await session.execute(query)).scalars().all()  # List[TrackDAO]

                result: List[Track] = await asyncio.gather(
                    *[track.from_domain()
                      for track in tracks]
                )
                return result
        except Exception as e:
            print(f"Error en get_all_album: {e}")
            return []

    async def get_track_by_id(self, track_id: int) -> Track:
        try:
            async with self.async_session() as session:
                query = (
                    select(TrackDAO)
                    .where(TrackDAO.TrackId == track_id)
                )

                track, *_ = (await session.execute(query)).scalars().all()  # List[TrackDAO]

                return await track.from_domain()
        except Exception as e:
            print(f"Error en get_all_album: {e}")
            raise e

    async def add_track(self, track: Track) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        await TrackDAO.from_dto(track)
                    ])
        except Exception as e:
            print(f"Error en get_all_tracks: {e}")
            raise e

    async def delete_track(self, id: int) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    await session.execute(
                        delete(TrackDAO).where(TrackDAO.TrackId == id)
                    )
        except Exception as e:
            print(f"Error in delete_track: {str(e)}")
            raise e

    async def update_track(self, track: Track) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    # Fetch the specific track object using fetchone
                    result = await session.execute(
                        select(TrackDAO).filter(TrackDAO.TrackId == track.id)
                    )
                    media_type_from_db = result.scalar()

                    # Check if track was found
                    if not media_type_from_db:
                        raise ValueError(f"Track with ID {id} not found")

                    # If the object is a SQLAlchemy model, update it using the update() method
                    if isinstance(media_type_from_db, TrackDAO):
                        await session.execute(
                            update(TrackDAO)
                            .where(TrackDAO.TrackId == track.id)
                            .values({
                                TrackDAO.TrackId: track.id,
                                TrackDAO.Name: track.name,
                                TrackDAO.Composer: track.composer,
                                TrackDAO.Milliseconds: track.miliseconds,
                                TrackDAO.Bytes: track.bytes,
                                TrackDAO.UnitPrice: track.unitprice,
                                TrackDAO.GenreId: track.genre.id,
                                TrackDAO.MediaTypeId: track.mediatype.id
                            }))
        except Exception as e:
            raise e

    async def get_tracks_from_album(self, album_id: int) -> List[Track]:
        try:
            async with self.async_session() as session:
                query = (select(TrackDAO)
                        .where(TrackDAO.AlbumId == album_id).options(
                        selectinload(TrackDAO.genre),
                        selectinload(TrackDAO.media_type))
                )

                tracks_album: List[TrackDAO] = (
                    await session.execute(query)
                ).scalars().all()  # List[TrackDAO]

                result: List[Track] = await asyncio.gather(*[
                    track.from_domain()
                    for track in tracks_album
                ])
                return result
        except Exception as e:
            print(f"Error in get_tracks_from_album: {e}")
            raise e

    async def get_tracks_from_playlist(self, playlist_id: int) -> List[Track]:
        try:
            async with self.async_session() as session:
                query = (
                    select(TrackDAO)
                    .join(PlayList_TrackDAO, PlayList_TrackDAO.TrackId == TrackDAO.TrackId)
                    .where(PlayList_TrackDAO.PlaylistId == playlist_id)
                    .options(
                        selectinload(TrackDAO.genre),
                        selectinload(TrackDAO.media_type)

                    ))

                tracks_pl: List[TrackDAO] = (await session.execute(query)).scalars().all()  # List[TrackDAO]

                result: List[Track] = [
                    await track.from_domain()
                    for track in tracks_pl
                ]

                return result
        except Exception as e:
            print(f"Error in get_tracks_from_playlist: {e}")
            raise e

    async def check_exist_tracks(self, tracks_ids: List[int]) -> bool:
        try:
            async with self.async_session() as session:
                query = select(TrackDAO.TrackId)
                track_all_ids: List[int] = (await session.execute(query)).scalars().all()  # List[int]

            return tracks_ids <= track_all_ids

        except Exception as e:
            print(f"Error en get_all_album: {str(e)}")
            raise e

from src.domain.repositories.genres_repository import GenreRepositories
from src.domain.repositories.media_type_repository import MediaTypeRepositories
from src.domain.repositories.track_repository import TrackRepository
from src.domain.models.track import Track
from src.infraestructure.entities.trackDAO import TrackDAO
from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories import engine
from sqlalchemy import select, delete, update
from pipe import Pipe, map


class TrackRepositoryImpl(TrackRepository):

    def __init__(self, media_type_repository: MediaTypeRepositories, genre_repository: GenreRepositories):
        super().__init__(media_type_repository, genre_repository)
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_all_tracks(self) -> List[Track]:
        try:
            async with self.async_session() as session:
                query = select(TrackDAO)
                genres = {f'{g.id}': g for g in (await self.genre_repository.get_all_genres())}
                media = {f'{m.id}': m for m in (await self.media_type_repository.get_all_media_type())}
                tracks = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[TrackDAO]
                    | Pipe(map(lambda t: Track( t.TrackId,
                                                t.Name,
                                                t.Composer,
                                                t.Milliseconds,
                                                t.Bytes,
                                                t.UnitPrice,
                                                genres[f'{t.GenreId}'],
                                                media[f'{t.MediaTypeId}'])))  # List[Track]
                )
                return tracks
        except Exception as e:
            print(f"Error en get_all_album: {str(e)}")
            return []

    async def get_track_by_id(self, track_id: int) -> Track:
        try:
            async with self.async_session() as session:
                query = select(TrackDAO).where(TrackDAO.TrackId == track_id)
                genres = {f'{g.id}': g for g in (await self.genre_repository.get_all_genres())}
                media = {f'{m.id}': m for m in (await self.media_type_repository.get_all_media_type())}
                tracks = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[TrackDAO]
                    | Pipe(map(lambda t: Track( t.TrackId,
                                                t.Name,
                                                t.Composer,
                                                t.Milliseconds,
                                                t.Bytes,
                                                t.UnitPrice,
                                                genres[f'{t.GenreId}'],
                                                media[f'{t.MediaTypeId}'])))  # List[Track]
                )
                return tracks[0]
        except Exception as e:
            print(f"Error en get_all_album: {str(e)}")
            return []       

    async def add_track(self, track: Track) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        TrackDAO(TrackId=track.id,
                                                Name=track.name,
                                                Composer=track.composer,
                                                Milliseconds=track.miliseconds,
                                                Bytes=track.quanty_bytes,
                                                UnitPrice=track.unitprice,
                                                GenreId=track.genre.id,
                                                MediaTypeId=track.mediatype.id)
                    ])
        except Exception as e:
            print(f"Error en get_all_tracks: {str(e)}")
            raise e

    async def delete_track(self, track: Track) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    session.execute(
                        delete(TrackDAO).where(TrackDAO.GenreId == track.id)
                    )
        except Exception as e:
            print(f"Error in delete_track: {str(e)}")
            raise e

    async def update_track(self, track: Track) -> None:
        pass

    async def get_tracks_from_album(self, album_id: int) -> List[Track]:
        try:
            async with self.async_session() as session:
                query = select(TrackDAO).where(TrackDAO.AlbumId == album_id)
                genres = {f'{g.id}': g for g in (await self.genre_repository.get_all_genres())}
                media = {f'{m.id}': m for m in (await self.media_type_repository.get_all_media_type())}
                tracks_album = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[TrackDAO]
                    | Pipe(map(lambda t: Track( t.TrackId,
                                                t.Name,
                                                t.Composer,
                                                t.Milliseconds,
                                                t.Bytes,
                                                t.UnitPrice,
                                                genres[f'{t.GenreId}'],
                                                media[f'{t.MediaTypeId}'])))  # List[Track]
                )
                return tracks_album
        except Exception as e:
            print(f"Error in get_tracks_from_album: {str(e)}")
            return []   

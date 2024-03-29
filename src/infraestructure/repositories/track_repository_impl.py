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
from src.infraestructure.entities.playlist_trackDAO import PlayList_TrackDAO

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
                   await session.execute(
                        delete(TrackDAO).where(TrackDAO.GenreId == track.id)
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
        
    async def get_tracks_from_playlist(self, playlist_id: int) -> List[Track]:
        try:
            async with self.async_session() as session:
                query = (
                        select(TrackDAO)
                        .join(PlayList_TrackDAO,PlayList_TrackDAO.TrackId == TrackDAO.TrackId)
                        .where(PlayList_TrackDAO.PlaylistId== playlist_id)
                        )
                
                genres = {f'{g.id}': g for g in (await self.genre_repository.get_all_genres())}
                media = {f'{m.id}': m for m in (await self.media_type_repository.get_all_media_type())}
                
                tracks_pl: List[Track] = list(
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
                return tracks_pl
        except Exception as e:
            print(f"Error in get_tracks_from_playlist: {str(e)}")
            return []
        
    async def check_exist_tracks(self, tracks_ids: List[int]) -> bool:
        try:
            async with self.async_session() as session:
                query = select(TrackDAO).where(TrackDAO.TrackId in tracks_ids)
                tracks = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[TrackDAO]
                )
                
                if len(tracks_ids) == len(tracks):   return True
                elif len(tracks_ids) != len(tracks): return False
                elif not tracks: return False
                else: return False
        
        except Exception as e:
            print(f"Error en get_all_album: {str(e)}")
            raise e 
            
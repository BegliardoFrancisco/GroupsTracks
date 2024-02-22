from src.domain.models.play_list import PlayList
from src.domain.repositories.playlist_repository import PlayListRepositories
from src.domain.repositories.playlist_track_repository import TracksInPlaylistRepository 
from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from . import engine
from sqlalchemy import select, delete, update
from src.infraestructure.entities.trackDAO import TrackDAO
from src.infraestructure.entities.playListDAO import PlayListDAO
from pipe import Pipe, map
from src.domain.repositories.track_repository import TrackRepository


class PlayListRepositoryImpl(PlayListRepositories):

    def __init__(self, track_repository: TrackRepository, track_in_playlist_repository: TracksInPlaylistRepository):
        super().__init__(track_repository, track_in_playlist_repository)
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_all_playlist(self) -> List[PlayList]:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    result = await session.execute(
                        select(PlayListDAO)
                    )
                    if not result | result == []:
                        raise ConnectionError(f"I don't know i can perform the search or this has not returned results")
                    playlists = result.scalars().all()
                
                    return [PlayList(playlist.PlaylistId, playlist.Name, None) for playlist in playlists]
        except Exception as e:
            print(f"Error in get_all_playlist: {e}")
            raise e 

    async def get_playlist_id(self, playlist_id: int) -> PlayList:
        try:
            if not isinstance(playlist_id, int) or not isinstance(playlist_id, float):
                raise ValueError(f"Parameter ID id not the right type")
            
            async with self.async_session() as session:
                query = select(PlayListDAO).where(PlayListDAO.PlaylistId == playlist_id)
                playlist: List[PlayList] = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[PlayListDAO]
                    | Pipe(map(lambda playlist: PlayList(playlist.PlaylistId, playlist.Name, None)))  # List[PlayList]
                )
                if not playlist | playlist == []:
                    raise ValueError(f" I don't know if I found any playlist with the ID provided")
                
                tracks_in_playlist = await self.track_repository.get_tracks_from_playlist(playlist[0].id)
                await playlist[0].add_tracks(tracks_in_playlist)

                return playlist[0]
        except Exception as e:
            print(f"Error in get_playlist_id: {str(e)}")
            raise e


    async def add_playlist(self, playlist: PlayList) -> None:
        try:
            if not isinstance(playlist, PlayList):
                 raise ValueError(f"Error in method update_playlist: don't provides params from type Playlist")
             
            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        PlayListDAO(
                            PlaylistId = playlist.id,
                            Name = playlist.name
                        )
                    ])
        except Exception as e:
            print(f"Error in add_playlist: {str(e)}")
            raise e


    async def delete_playlist(self, playlist_id: int) -> None:
        try:
            if not isinstance(playlist_id, int) or not isinstance(playlist_id, float):
                raise ValueError(f"Parameter ID id not the right type")
            
            async with self.async_session() as session:
                async with session.begin():
                    await session.execute(
                        delete(PlayListDAO).where(PlayListDAO.PlaylistId == playlist_id)
                    )
        except Exception as e:
            print(f"Error in delete_playlist: {str(e)}")
            raise e
        
    async def update_playlist(self, playlist: PlayList) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    # Fetch the specific playlist object using fetchone
                    result = await session.execute(
                        select(PlayListDAO).filter(PlayListDAO.PlaylistId == playlist.id)
                    )
                    play_list_from_db = result.scalar()

                    # Check if Playlist was found
                    if not play_list_from_db:
                        raise ValueError(f"PlayList with ID {id} not found")

                    # If the object is a SQLAlchemy model, update it using the update() method
                    if isinstance(play_list_from_db, PlayListDAO):
                        await session.execute(
                            update(PlayListDAO)
                            .where(PlayListDAO.PlaylistId == playlist.id)
                            .values({
                                    PlayListDAO.PlaylistId: playlist.id,
                                    PlayListDAO.Name: playlist.name
                        }))
                    else: 
                        raise TypeError(f'You are operating on the wrong table {__class__}')
        except Exception as e:
            print(f"Error in update_playlist: {e}")
            raise e            
    
    async def add_track_from_playlist(self, track_id: int, playlist_id: int) -> None:
        try:
            if self.track_repository.check_exist_tracks([track_id]) and self.check_exist_playlist(playlist_id):     
                await self.track_in_pl.add_track_from_playlist(track_id, playlist_id)
            else: 
                raise ValueError(f"Track Id is invalid")
        except Exception as e:
            raise e
    
    async def add_tracks_from_playlist(self, tracks_id: List[int], playlist_id: int) -> None:
        try:
            if self.track_repository.check_exist_tracks(tracks_id) and self.check_exist_playlist(playlist_id):     
                await self.track_in_pl.add_tracks_from_playlist(tracks_id, playlist_id)
            else: 
                raise ValueError(f"Tracks Id is invalid")        
        except Exception as e:
            raise e
    
    async def delete_track_from_playlist(self, track_id: int, playlist_id: int) -> None:
        try:
            if self.track_repository.check_exist_tracks([track_id]) and self.check_exist_playlist(playlist_id):
                await self.track_in_pl.delete_track_from_playlist(track_id, playlist_id)
            else:
                raise ValueError(f"Track Id is invalid")          
        except Exception as e:
            raise e
    
    async def delete_tracks_from_playlist(self, tracks_id: List[int], playlist_id: int) -> None:
        try:
            if self.track_repository.check_exist_tracks(tracks_id) and self.check_exist_playlist(playlist_id):
                await self.track_in_pl.delete_tracks_from_playlist(tracks_id, playlist_id)
            else:
                raise ValueError(f"Tracks Id is invalid")          
        except Exception as e:
            raise e
        
    async def check_exist_playlist(self, playlist_id: int | float) -> bool:
        
        try:
            if not isinstance(playlist_id,int) or not isinstance(playlist_id, float):
                raise ValueError(f"Parameter ID id not the right type")
            
            async with self.async_session() as session:
                query = select(PlayListDAO).where(PlayListDAO.PlaylistId == playlist_id)
                playlist: List[PlayList] = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[PlayListDAO]
                )
                
                if not playlist: return False
                else: return True
                
                
        except Exception as e:
            print(f"Error in get_playlist_id: {str(e)}")
            raise e
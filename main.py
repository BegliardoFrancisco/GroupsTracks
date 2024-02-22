from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from typing import List
from src.infraestructure.repositories.album_repository_impl import AlbumRepositoryImpl
from src.infraestructure.repositories.artist_repository_impl import ArtistRepositoryImpl
from src.infraestructure.repositories.track_repository_impl import TrackRepositoryImpl
from src.infraestructure.repositories.genre_repository_impl import GenreRepositoryImpl
from src.infraestructure.repositories.media_type_repository_impl import MediaTypeRepositoryImpl
from src.infraestructure.repositories.playlist_repository_impl import PlayListRepositoryImpl
from src.infraestructure.repositories.track_in_playlist_repository import TracksInPlaylistRepositoryImpl
from src.domain.models.track import Track
from src.domain.models.media_type import MediaType
from src.infraestructure.repositories import engine
from src.infraestructure.entities.trackDAO import TrackDAO
from src.domain.models.play_list import PlayList
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from src.domain.models.artist import Artist
from src.domain.models.album import Album

async def conn_bdd():
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with async_session() as session:
        query = select(TrackDAO)
        execute = await session.execute(
            query
        )
        result: List[TrackDAO] = execute.scalars().all()


mt = MediaTypeRepositoryImpl()
g = GenreRepositoryImpl()
t = TrackRepositoryImpl(mt, g)
pl_t = TracksInPlaylistRepositoryImpl(t)
genre = PlayListRepositoryImpl(t,pl_t )

alb = AlbumRepositoryImpl()
art = ArtistRepositoryImpl()

async def todo(gen: PlayListRepositoryImpl):
    ges: List[PlayList] = [await gen.get_playlist_id(4)]
    for ge in ges:
        tracks = [f' \n name: {t.name} id: {t.id} \n' for t in ge.tracks]
        
        print('{' + f'name: {ge.name}, id: {ge.id} '+ '}')
        
        for t in tracks:
            print(t) 
        
        if len(tracks) == 0:
            print('vacio')
            
async def add_p(gen : PlayListRepositoryImpl):
    ges = await gen.add_playlist(PlayList(100,'Nueva Vida de Luna', None))

async def update_p(gen: PlayListRepositoryImpl):
    ges= await gen.update_playlist(PlayList(100,'Nueva Vida De Luna', None))
    
async def delete_p(gen: PlayListRepositoryImpl):
    ges= await gen.delete_playlist(100)
    
async def track_get(gen: TrackRepositoryImpl):
    ges = await gen.get_all_tracks()
    for ge in ges:
        print('{' + f'name: {ge.name}, id: {ge.id}'+ '}')  

async def get_t_pl(gen: PlayListRepositoryImpl):
    ges = await gen.delete_tracks_from_playlist([3503,3502,3501],4)
    
async def get_artist(gen: ArtistRepositoryImpl):
   a: List[Artist] = await gen.get_all_artist()
   for i in a:
       print(f'Id:{i.id} Name:{i.name}')    
       

async def delete_artist(gen: ArtistRepositoryImpl):
    await gen.delete_artist(316)
    
async def get_albums_from_artist(gen: AlbumRepositoryImpl):
    a: List[Album] = await gen.get_albums_from_artist(376)
    for i in a:
        print(f'Id:{i.id} Name:{i.title}')    
        
asyncio.run(get_albums_from_artist(alb))

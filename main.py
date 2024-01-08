from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from typing import List
from src.infraestructure.repositories.track_repository_impl import TrackRepositoryImpl
from src.infraestructure.repositories.genre_repository_impl import GenreRepositoryImpl
from src.infraestructure.repositories.media_type_repository_impl import MediaTypeRepositoryImpl
from src.infraestructure.repositories.playlist_repository_impl import PlayListRepositoryImpl
from src.domain.models.track import Track
from src.domain.models.media_type import MediaType
from src.infraestructure.repositories import engine
from src.infraestructure.entities.trackDAO import TrackDAO
from src.domain.models.play_list import PlayList
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio




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
t = TrackRepositoryImpl(mt,g)

genre = PlayListRepositoryImpl(g, mt)


async def todo(gen):
    ges: List[PlayList] = await gen.get_all_playlist()
    for ge in ges:
        tracks = [f'Name: {t.name}' for t in gen.tracks ]
        print('{' + f'name: {ge.name}, id: {ge.id} , tracks: {tracks} ' + '}')


async def printer(gen: TrackRepositoryImpl):
    media = MediaType(6, 'WAV')
    await gen.update_media_type(media)


asyncio.run(todo(genre))

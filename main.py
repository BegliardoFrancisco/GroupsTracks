from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from typing import List
from src.infraestructure.repositories.genre_repository_impl import GenreRepositoryImpl
from src.domain.models.play_list import PlayList
from src.domain.models.media_type import MediaType
from src.infraestructure.repositories import engine
from src.infraestructure.entities.trackDAO import TrackDAO
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from src.infraestructure.repositories.media_type_repository_impl import MediaTypeRepositoryImpl



async def conn_bdd():
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with async_session() as session:
        query = select(TrackDAO)
        execute = await session.execute(
            query
        )
        result: List[TrackDAO] = execute.scalars().all()

        for a in result:
            print("{" + f' id: {a.TrackId},\n  artist: {a.Milliseconds},\n  album: {a.AlbumId},\n' + '}')


genre = GenreRepositoryImpl()


async def todo(gen):
    ges: List[PlayList] = await gen.get_all_genres()
    for ge in ges:
        tracks = [f'{t.name}' for t in ge.tracks]
        print('{' + f'name: {ge.name}, id: {ge.id} ' + '}')


async def printer(gen: MediaTypeRepositoryImpl):
    media = MediaType(6, 'WAV')
    await gen.update_media_type(media)


asyncio.run(todo(genre))

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from typing import List

from src.domain.models.album import Album
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


genre = MediaTypeRepositoryImpl()


async def todo(gen):
    ges: List[MediaType] = [await gen.get_media_type_id(6)]
    for ge in ges:
        print('{' + f'name: {ge.name}, id: {ge.id} ' + '}')


async def printer(gen: MediaTypeRepositoryImpl):
    media = MediaType(6, 'WAV')
    await gen.update_media_type(media)






asyncio.run(todo(genre))

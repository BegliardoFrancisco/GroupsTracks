from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from typing import List
from src.infraestructure.repositories.track_repository_impl import TrackRepositoryImpl
from src.infraestructure.repositories.genre_repository_impl import GenreRepositoryImpl
from src.infraestructure.repositories.media_type_repository_impl import MediaTypeRepositoryImpl
from src.domain.models.track import Track
from src.domain.models.media_type import MediaType
from src.infraestructure.repositories import engine
from src.infraestructure.entities.trackDAO import TrackDAO
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
genre = TrackRepositoryImpl(mt,g)


async def todo(gen):
    ges: List[Track] = [await gen.get_track_by_id(1)]
    for ge in ges:
        print('{' + f'name: {ge.name}, id: {ge.id} ' + '}')


async def printer(gen: TrackRepositoryImpl):
    media = MediaType(6, 'WAV')
    await gen.update_media_type(media)


asyncio.run(todo(genre))

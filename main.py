from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from typing import List

from src.domain.models.artist import Artist
from src.infraestructure.repositories import engine
from src.infraestructure.entities.trackDAO import TrackDAO
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from src.infraestructure.repositories.artist_repository_impl import ArtistRepositoryImpl


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


genre = ArtistRepositoryImpl()


async def todo(gen):
    ges: List[Artist] = await gen.get_all_artist()
    for ge in ges:
        print('{' + f'name: {ge.name}, id: {ge.id}' + '}')


async def printer(gen: ArtistRepositoryImpl):
    artist = Artist(id=316, name="Francisco", albums=None)
    await gen.update_artist(artist=artist, id=316)


async def main(gen):
    print('AFTER')
    await todo(gen)
    print('UPDATE')
    await printer(gen)
    print('BEFORE')
    await todo(gen)


asyncio.run(main(genre))

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, Any
from typing import List

from src.infraestructure.entities.trackDAO import TrackDAO
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import asyncio


async def conn_bdd():
    engine = create_async_engine("sqlite+aiosqlite:///chinook.db", echo=True)

    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with async_session() as session:
        query = select(TrackDAO)
        print('aca', query)

        arti = await session.execute(
            query
        )
        result: List[TrackDAO] = arti.scalars().all()

        for a in result:
            print("{" + f' id: {a.TrackId},\n  artist: {a.Milliseconds},\n  album: {a.AlbumId},\n' + '}')
asyncio.run(conn_bdd())

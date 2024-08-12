import asyncio
from datetime import datetime

from sqlalchemy.exc import IntegrityError

from src.domain.models.artist import Artist
from src.domain.repositories.artist_repository import ArtistRepositories
from src.infraestructure.entities.artistDAO import ArtistDAO
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine
from typing import List
from sqlalchemy import select, delete, update


class ArtistRepositoryImpl(ArtistRepositories):

    def __init__(self, ):
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_all_artist(self) -> List[Artist]:
        try:
            async with self.async_session() as session:
                query = select(ArtistDAO)
                artists = (await session.execute(query)).scalars().all()  # List[ArtistDAO]

                if not artists or artists == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                result: List[Artist] = await asyncio.gather(
                    *[artist.from_domain()
                      for artist in artists]
                )

                return result
        except Exception as e:
            print(f"Error in get_all_artist: {e}")
            raise e

    async def get_artist_id(self, id: int) -> Artist:
        try:
            if not isinstance(id, int):
                raise AttributeError(f"id no is instance of int")

            async with self.async_session() as session:
                query = select(ArtistDAO).where(ArtistDAO.ArtistId == id)
                artist, *_ = (await session.execute(query)).scalars().all()  # Convert in type List[ArtistDAO]

                if not artist:
                    raise ValueError(f" I don't know if I found any artist with the ID provided")

                result = await artist.from_domain()

                return result
        except Exception as e:
            print(f"Error in get_artist_id: {e}")
            raise e

    async def add_artist(self, artist: Artist) -> None:

        try:
            if not isinstance(artist, Artist):
                raise ValueError(f"provides incorrect data for the add_artist method")

            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        await ArtistDAO.from_dto(artist)
                    ])
        except IntegrityError as id_error:
            print(f'{datetime.now()} {id_error}')
            raise ValueError('The Artist ID already exists')
        except Exception as e:
            print(f'{e}')
            raise e

    async def delete_artist(self, artist_id: int) -> None:
        try:
            if not isinstance(artist_id, int):
                raise AttributeError(f"id no is instance of int")

            async with self.async_session() as session:
                async with session.begin():
                    await session.execute(
                        delete(ArtistDAO)
                        .where(ArtistDAO.ArtistId == artist_id)
                    )
        except Exception as e:
            print(f"Error in delete_artist: {str(e)}")
            raise e

    async def update_artist(self, artist: Artist) -> None:
        try:

            if not isinstance(artist, Artist):
                raise ValueError(f"Error in method update_artist: don't provides params from type Artist")

            async with self.async_session() as session:

                async with session.begin():
                    # Fetch the specific artist object using fetchone
                    result = await session.execute(
                        select(ArtistDAO).filter(ArtistDAO.ArtistId == artist.id)
                    )
                    artist_from_db = result.scalar()

                    # Check if artist was found
                    if not artist_from_db:
                        raise ValueError(f"Artist with ID {id} not found")

                    # If the object is a SQLAlchemy model, update it using the update() method
                    if isinstance(artist_from_db, ArtistDAO):
                        await session.execute(
                            update(ArtistDAO)
                            .where(ArtistDAO.ArtistId == artist.id)
                            .values({
                                ArtistDAO.ArtistId: artist.id,
                                ArtistDAO.Name: artist.name
                            })
                        )

        except Exception as e:
            raise e

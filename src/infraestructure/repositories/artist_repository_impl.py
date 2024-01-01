
from src.domain.models.artist import Artist
from src.domain.repositories.artist_repository import ArtistRepositories
from src.infraestructure.entities.artistDAO import ArtistDAO
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine
from pipe import Pipe, map
from typing import List
from sqlalchemy import select, delete, update


class ArtistRepositoryImpl(ArtistRepositories):

    def __init__(self,):
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_all_artist(self) -> List[Artist]:
        try:
            async with self.async_session() as session:
                query = select(ArtistDAO)
                artists = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[ArtistDAO]
                    | Pipe(map(lambda artist: Artist(artist.ArtistId, artist.Name, None)))  # List[Artist]
                )
                return artists
        except Exception as e:
            print(f"Error en get_all_genres: {str(e)}")
            return []

    async def get_artist_id(self, id: int) -> Artist:
        try:
            async with self.async_session() as session:
                query = select(ArtistDAO).where(ArtistDAO.ArtistId == id)
                genre = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # Convert in type List[ArtistDAO]
                    | Pipe(map(lambda genre_dao: Artist(genre_dao.ArtistId, genre_dao.Name)))  # List[Artist]
                )
                return genre[0]
        except Exception as e:
            print(f"Error en get_all_genres: {str(e)}")
            raise e

    async def add_artist(self, artist: Artist) -> None:

        try:
            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        ArtistDAO(ArtistId=artist.id, Name=artist.name)
                    ])
        except Exception as e:
            print(f"Error en get_all_artist: {str(e)}")
            raise e

    async def delete_artist(self, artist: Artist) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    await session.execute(
                        delete(ArtistDAO)
                        .where(ArtistDAO.ArtistId == artist.id)
                    )
        except Exception as e:
            print(f"Error en get_all_artist: {str(e)}")
            raise e

    async def update_artist(self, artist: Artist, id: int) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    # Fetch the specific artist object using fetchone
                    result = await session.execute(
                        select(ArtistDAO).filter(ArtistDAO.ArtistId == id)
                    )
                    artist_from_db = result.scalar()

                    # Check if artist was found
                    if not artist_from_db:
                        raise ValueError(f"Artist with ID {id} not found")

                    # If the object is a SQLAlchemy model, update it using the update() method
                    if isinstance(artist_from_db, ArtistDAO):
                        await session.execute(
                            update(ArtistDAO)
                            .where(ArtistDAO.ArtistId == id)
                            .values({
                                ArtistDAO.ArtistId: artist.id,
                                ArtistDAO.Name: artist.name
                            })
                        )
        except Exception as e:
            raise e


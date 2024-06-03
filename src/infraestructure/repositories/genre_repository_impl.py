import asyncio

from typing import List
from sqlalchemy import select, delete
from src.domain.models.genre import Genre
from src.domain.repositories.genres_repository import GenreRepositories
from src.infraestructure.entities.genresDAO import GenresDAO
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine


class GenreRepositoryImpl(GenreRepositories):

    def __init__(self):
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_all_genres(self) -> List[Genre]:
        try:
            async with self.async_session() as session:
                query = select(GenresDAO)
                genres = (await session.execute(query)).scalars().all()  # List[GenreDAO]

                if not genres or genres == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                result: List[Genre] = await asyncio.gather(
                    *[genre.from_domain() for genre in genres]
                )

                return result
        except Exception as e:
            print(f"Error in get_all_genres: {e}")
            raise e

    async def get_genres_id(self, id: int) -> Genre:
        try:
            if not isinstance(id, int):
                raise ValueError(f"Parameter ID id not the right type")

            async with self.async_session() as session:
                query = select(GenresDAO).where(GenresDAO.GenreId == id)
                genre, *others = (await session.execute(query)).scalars().all()  # List[GenreDAO]

                if not genre:
                    raise ValueError(f" I don't know if I found any genre with the ID provided")

                return await genre.from_domain()
        except Exception as e:
            print(f"Error in get_genres_id: {e}")
            raise e

    async def add_genres(self, genre: Genre) -> None:
        try:
            if not isinstance(genre, Genre):
                raise ValueError(f"It doesn´t an objet Genre")

            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        await GenresDAO.from_dto(genre)
                    ])
        except Exception as e:
            print(f"Error in add_genres: {e}")
            raise e

    async def delete_genres(self, id: int) -> None:
        try:
            async with self.async_session() as session:
                query = delete(GenresDAO).where(GenresDAO.GenreId == id)
                async with session.begin():
                    await session.execute(
                       query
                    )
        except Exception as e:
            print(f"Error in delete_genres: {e}")
            raise e

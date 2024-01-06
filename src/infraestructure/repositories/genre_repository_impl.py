from typing import List
from sqlalchemy import select, delete
from src.domain.models.genre import Genre
from src.domain.repositories.genres_repository import GenreRepositories
from src.infraestructure.entities.genresDAO import GenresDAO
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine
from pipe import Pipe, map


class GenreRepositoryImpl(GenreRepositories):

    def __init__(self):
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    
    async def get_all_genres(self) -> List[Genre]:
        try:
            async with self.async_session() as session:
                query = select(GenresDAO)
                genres = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[GenreDAO]
                    | Pipe(map(lambda genre_dao: Genre(genre_dao.GenreId, genre_dao.Name)))  # List[Genre]
                )
                return genres
        except Exception as e:
            print(f"Error en get_all_genres: {str(e)}")
            return []

    async def get_genres_id(self, id: int) -> Genre:
        try:
            async with self.async_session() as session:
                query = select(GenresDAO).where(GenresDAO.GenreId == id)
                genre = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[GenreDAO]
                    | Pipe(map(lambda genre_dao: Genre(genre_dao.GenreId, genre_dao.Name)))  # List[Genre]
                )
                return genre[0]
        except Exception as e:
            print(f"Error en get_all_genres: {str(e)}")
            raise e

    async def add_genres(self, genre: Genre) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        GenresDAO(GenreId=genre.id, Name=genre.name)
                    ])
        except Exception as e:
            print(f"Error en get_all_genres: {str(e)}")
            raise e

    async def delete_genres(self, genres: Genre) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    session.execute(
                        delete(GenresDAO).where(GenresDAO.GenreId == genres.id)
                    )

        except Exception as e:
            print(f"Error en get_all_genres: {str(e)}")
            raise e

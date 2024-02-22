from src.domain.models.album import Album
from src.infraestructure.entities.albumDAO import AlbumDAO
from src.domain.repositories.album_repository import AlbumRepositories
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine
from pipe import Pipe, map
from typing import List
from sqlalchemy import select, delete, update


class AlbumRepositoryImpl(AlbumRepositories):
    def __init__(self):
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_all_album(self) -> List[Album]:
        try:
            async with self.async_session() as session:
                query = select(AlbumDAO)
                albums = list(
                await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[AlbumDAO]
                    | Pipe(map(lambda abm: Album(abm.AlbumId, abm.title, None)))  # List[Album]
                )
                if not albums | albums == []:
                   raise ConnectionError(f"I don't know i can perform the search or this has not returned results")
             
                return albums
        except Exception as e:
            print(f"Error in get_all_album: {e}")
            raise e

    async def get_albums_from_artist(self, artist_id: int) -> List[Album]:
        try:
            
            if not isinstance(artist_id, int) or not isinstance(artist_id, int):
                raise AttributeError(f"artist_id no is instance of int or float type")
            
            async with self.async_session() as session:
                query = select(AlbumDAO).where(AlbumDAO.ArtistId == artist_id)
                albums: List[Album] = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[AlbumDAO]
                    | Pipe(map(lambda a: Album(a.AlbumId, a.title, None)))  # List[Album]
                )
                if not albums: 
                    raise ValueError(f"The ID from artist provided does not correspond to any record")
                return albums  
        except Exception as e:
            print(f"Error in get_albums_from_album: {e}")
            raise e

    async def get_album_id(self, id: int) -> Album:
        try:
            if not isinstance(id, int) or not isinstance(id, int):
                raise AttributeError(f"artist_id no is instance of int or float type")
            
            async with self.async_session() as session:
                query = select(AlbumDAO).where(AlbumDAO.AlbumId == id)
                albums: List[Album] = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[AlbumDAO]
                    | Pipe(map(lambda a: Album(a.AlbumId, a.title, None)))  # List[Album]
                )
                if not albums: 
                    raise ValueError(f"The ID from album provided does not correspond to any record")
                return albums[0]
        except Exception as e:
            print(f"Error in get_album_id: {e}")
            raise e

    async def add_album(self, album: Album, artist_id: int) -> None:
        try:
            if not isinstance(artist_id, int) or not isinstance(artist_id, int):
                raise AttributeError(f"artist_id no is instance of int or float type")
            
            if not isinstance(album, Album) or not isinstance(album, Album):
                raise AttributeError(f"thee album prop in metdhos not is type Album")
            
            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        AlbumDAO(AlbumId=album.id, title=album.title, ArtistId=artist_id)
                    ])
                    
        except Exception as e:
            print(f"Error in add_album: {str(e)}")
            raise e

    async def delete_album(self, album_id: int) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    await session.execute(
                        delete(AlbumDAO)
                        .where(AlbumDAO.AlbumId == album_id)
                    )
        except Exception as e:
            print(f"Error in delete_album: {str(e)}")
            raise e

    async def update_album(self, album: Album, artist_id: int) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    # Fetch the specific album object using fetchone
                    result = await session.execute(
                        select(AlbumDAO).filter(AlbumDAO.AlbumId == album.id)
                    )
                    album_from_db = result.scalar()

                    # Check if album was found
                    if not album_from_db:
                        raise ValueError(f"Artist with ID {id} not found")

                    # If the object is a SQLAlchemy model, update it using the update() method
                    if isinstance(album_from_db, AlbumDAO):
                        await session.execute(
                            update(AlbumDAO)
                            .where(AlbumDAO.AlbumId == album.id)
                            .values({
                                AlbumDAO.AlbumId: album.id,
                                AlbumDAO.title: album.title,
                                AlbumDAO.ArtistId: artist_id
                            })
                        )
        except Exception as e:
            raise e

    async def get_artist_id_from_album(self, album: Album) -> int:
        try:
            async with self.async_session() as session:
                query = select(AlbumDAO.ArtistId).where(AlbumDAO.AlbumId == album.id)

                artist_id = (
                    await session.execute(query)
                ).scalar()

                if not artist_id:
                    raise ValueError(f"Album with ID {id} not found")

                return artist_id

        except Exception as e:
            raise e

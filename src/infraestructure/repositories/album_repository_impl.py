import asyncio

from src.domain.models.album import Album
from src.infraestructure.entities.albumDAO import AlbumDAO
from src.domain.repositories.album_repository import AlbumRepositories
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.entities.artistDAO import ArtistDAO
from src.infraestructure.repositories import engine
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
                albums = (await session.execute(query)).scalars().all()  # List[AlbumDAO]

                if not albums or albums == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                result: List[Album] = await asyncio.gather(
                    *[album.from_domain()
                      for album in albums]
                )

                return result
        except Exception as e:
            print(f"Error in get_all_album: {e}")
            raise e

    async def get_albums_from_artist(self, artist_id: int) -> List[Album]:
        try:

            if not isinstance(artist_id, int):
                raise AttributeError(f"artist_id {artist_id} no is instance of int")

            async with self.async_session() as session:

                query = select(AlbumDAO).where(AlbumDAO.ArtistId == artist_id)
                check = select(ArtistDAO.ArtistId).where(ArtistDAO.ArtistId == artist_id)

                checking: int = (await session.execute(check)).scalar()
                if not checking:
                    raise ValueError(f"The ID {artist_id} from artist provided does not correspond to any record")

                albums: List[AlbumDAO] = (await session.execute(query)).scalars().all()

                if not albums or albums == []:
                    return []

                result: List[Album] = [
                    await album.from_domain()
                    for album in albums]

                return result

        except Exception as e:
            print(f"Error in get_albums_from_artist: {e}")
            raise e

    async def get_album_id(self, album_id: int) -> Album:
        try:
            if not isinstance(album_id, int):
                raise AttributeError(f"album_id no is instance of int")

            async with self.async_session() as session:
                query = select(AlbumDAO).where(AlbumDAO.AlbumId == album_id)

                album, *_ = (await session.execute(query)).scalars().all()  # List[AlbumDAO]

                if not album:
                    raise ValueError(f"The ID from album provided does not correspond to any record")

                result: Album = await album.from_domain()

                return result

        except Exception as e:
            print(f"Error in get_album_id: {e}")
            raise e

    async def add_album(self, album: Album, artist_id: int) -> None:
        try:
            if not isinstance(artist_id, int):
                raise AttributeError(f"artist_id not is instance of int")

            if not isinstance(album, Album):
                raise AttributeError(f"the album prop in method not is type Album")

            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        await AlbumDAO.from_dto(album, artist_id)
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

from src.domain.models.media_type import MediaType
from src.domain.repositories.media_type_repository import MediaTypeRepositories
from src.infraestructure.entities import TrackDAO
from src.infraestructure.entities.media_typesDAO import MediaTypeDAO
from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine
from pipe import Pipe, map
from sqlalchemy import select, delete, update


class MediaTypeRepositoryImpl(MediaTypeRepositories):

    def __init__(self):
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_all_media_type(self) -> List[MediaType]:
        try:
            async with self.async_session() as session:
                query = select(MediaTypeDAO)
                mediatypes = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[MediaTypeDAO]
                    | Pipe(map(lambda media_type: MediaType(media_type.MediaTypeId, media_type.Name)))
                    # List[MediaType]
                )

                return mediatypes
        except Exception as e:
            print(f"Error en get_all_genres: {str(e)}")
            return []

    async def get_media_type_id(self, id: int) -> MediaType:
        try:

            async with self.async_session() as session:
                query = select(MediaTypeDAO).where(MediaTypeDAO.MediaTypeId == id)
                mediatypes = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[MediaTypeDAO]
                    | Pipe(map(lambda media_type: MediaType(media_type.MediaTypeId, media_type.Name)))
                    # List[MediaType]
                )
                return mediatypes[0]
        except Exception as e:
            print(f"Error en get_all_genres: {str(e)}")
            raise e

    async def add_media_type(self, media_type: MediaType) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        MediaTypeDAO(MediaTypeId=media_type.id, Name=media_type.name)
                    ])
        except Exception as e:
            print(f"Error en get_all_genres: {str(e)}")
            raise e

    async def delete_media_type(self, media_type: MediaType) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    session.execute(
                        delete(MediaTypeDAO).where(MediaTypeDAO.MediaTypeId == media_type.id)
                    )
        except Exception as e:
            print(f"Error en get_all_genres: {str(e)}")
            raise e

    async def update_media_type(self, media_type: MediaType) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    # Fetch the specific mediatype object using fetchone
                    result = await session.execute(
                        select(MediaTypeDAO).filter(MediaTypeDAO.MediaTypeId == media_type.id)
                    )
                    media_type_from_db = result.scalar()

                    # Check if artist was found
                    if not media_type_from_db:
                        raise ValueError(f"Artist with ID {id} not found")

                    # If the object is a SQLAlchemy model, update it using the update() method
                    if isinstance(media_type_from_db, MediaTypeDAO):
                        await session.execute(
                            update(MediaTypeDAO)
                            .where(MediaTypeDAO.MediaTypeId == media_type.id)
                            .values({
                                MediaTypeDAO.MediaTypeId: media_type.id,
                                MediaTypeDAO.Name: media_type.name
                            })
                        )
        except Exception as e:
            raise e

    async def get_media_type_from_track(self, track_id: int) -> MediaType:
        try:
            async with self.async_session() as session:
                query = select(MediaTypeDAO).join(TrackDAO, TrackDAO.MediaTypeId == MediaTypeDAO.MediaTypeId).where(
                    TrackDAO.TrackId == track_id)
                mediatype = await session.execute(query)  # List[Tuple]
                mediatype: MediaTypeDAO = mediatype.scalars().all()  # MediaTypeDAO
                result: MediaType = MediaType(mediatype[0].MediaTypeId, mediatype[0].Name)  # List[MediaType]

                return result
        except Exception as e:
            print(f"Error en get_all_genres: {str(e)}")
            raise e

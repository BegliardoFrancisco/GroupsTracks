import asyncio
from src.domain.models.media_type import MediaType
from src.domain.repositories.media_type_repository import MediaTypeRepositories
from src.infraestructure.entities.trackDAO import TrackDAO
from src.infraestructure.entities.media_typesDAO import MediaTypeDAO
from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine
from pipe import Pipe
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
                )
                if not mediatypes or mediatypes == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                result: List[MediaType] = await asyncio.gather(*[mediatype.from_domain() for mediatype in mediatypes])

                return result

        except Exception as e:
            print(f"Error in get_all_media_type: {e}")
            raise e

    async def get_media_type_id(self, id: int) -> MediaType:
        try:
            print(type(id))
            if not isinstance(id, int) or isinstance(id, float):
                raise ValueError(f"Parameter ID id not the right type")

            async with self.async_session() as session:
                query = select(MediaTypeDAO).where(MediaTypeDAO.MediaTypeId == id)

                mediatype, *_ = (await session.execute(query)).scalars().all()  # List[MediaTypeDAO]

                if not mediatype:
                    raise ValueError(f" I don't know if I found any mediatype with the ID provided")

                return await mediatype.from_domain()

        except Exception as e:
            print(f"Error in get_media_type_id: {e}")
            raise e

    async def add_media_type(self, media_type: MediaType) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        await MediaTypeDAO.from_dto(media_type)
                    ])
        except Exception as e:
            print(f"Error in add_media_type: {e}")
            raise e

    async def delete_media_type(self, id: int) -> None:
        try:

            if not isinstance(id, int):
                raise ValueError(f"Parameter ID id not the right type")

            async with self.async_session() as session:
                query = delete(MediaTypeDAO).where(MediaTypeDAO.MediaTypeId == id)
                async with session.begin():

                    await session.execute(query)

        except Exception as e:
            print(f"Error in delete_media_type: {str(e)}")
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
                        raise ValueError(f"MediaType with ID {id} not found")

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
            if not isinstance(track_id, int):
                raise ValueError(f"Parameter ID id not the right type")

            async with self.async_session() as session:
                query = (select(MediaTypeDAO)
                         .join(TrackDAO, TrackDAO.MediaTypeId == MediaTypeDAO.MediaTypeId)
                         .where(TrackDAO.TrackId == track_id))

                mediatype, *_ = (await session.execute(query)).scalars().all()  # List[Tuple]

                if not mediatype:
                    raise ValueError(f" I don't know if I found any mediatype with the ID_Track provided")

                return await mediatype.from_domain()

        except Exception as e:
            print(f"Error in get_media_type_from_track: {e}")
            raise e

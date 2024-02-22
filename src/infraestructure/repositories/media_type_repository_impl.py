from src.domain.models.media_type import MediaType
from src.domain.repositories.media_type_repository import MediaTypeRepositories
from src.infraestructure.entities.trackDAO import TrackDAO
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
                if not mediatypes | mediatypes == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")
                return mediatypes
        except Exception as e:
            print(f"Error in get_all_media_type: {e}")
            return []

    async def get_media_type_id(self, id: int) -> MediaType:
        try:
            if not isinstance(id,int) or not isinstance(id,float):
                raise ValueError(f"Parameter ID id not the right type")
            
            async with self.async_session() as session:
                query = select(MediaTypeDAO).where(MediaTypeDAO.MediaTypeId == id)
                mediatypes = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[MediaTypeDAO]
                    | Pipe(map(lambda media_type: MediaType(media_type.MediaTypeId, media_type.Name)))
                    # List[MediaType]
                )
                
                if not mediatypes | mediatypes == []:
                    raise ValueError(f" I don't know if I found any mediatypes with the ID provided")
                
                return mediatypes[0]
        except Exception as e:
            print(f"Error in get_media_type_id: {e}")
            raise e

    async def add_media_type(self, media_type: MediaType) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        MediaTypeDAO(MediaTypeId=media_type.id, Name=media_type.name)
                    ])
        except Exception as e:
            print(f"Error in add_media_type: {e}")
            raise e

    async def delete_media_type(self, media_type: MediaType) -> None:
        try:
            if not isinstance(media_type, MediaType): 
                raise ValueError(f"It doesn´t an objet MediaType")
            
            async with self.async_session() as session:
                async with session.begin():
                    session.execute(
                        delete(MediaTypeDAO).where(MediaTypeDAO.MediaTypeId == media_type.id)
                    )
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
            if not isinstance(track_id,int) or not isinstance(track_id,float):
                raise ValueError(f"Parameter ID id not the right type")
            
            async with self.async_session() as session:
                query = (select(MediaTypeDAO)
                        .join(TrackDAO, TrackDAO.MediaTypeId == MediaTypeDAO.MediaTypeId)
                        .where(TrackDAO.TrackId == track_id))
                mediatype = await session.execute(query)  # List[Tuple]
                
                if not mediatype | mediatype == []:
                    raise ValueError(f" I don't know if I found any mediatypes with the ID_Track provided")
                
                mediatype: MediaTypeDAO = mediatype.scalars().all()  # MediaTypeDAO
                result: MediaType = MediaType(mediatype[0].MediaTypeId, mediatype[0].Name)  # List[MediaType]

                return result
        except Exception as e:
            print(f"Error in get_media_type_from_track: {e}")
            raise e

from src.infraestructure.entities.base import Base
from typing import Dict
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from src.domain.models.media_type import MediaType


class MediaTypeDAO(Base):
    __tablename__ = "media_types"
    MediaTypeId: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str]

    async def from_domain(self, ) -> MediaType:
        return MediaType(
            id=self.MediaTypeId,
            name=self.Name
        )

    @staticmethod
    async def from_dto(mediatype: MediaType) -> 'MediaTypeDAO':
        return MediaTypeDAO(
            MediaTypeId=mediatype.id,
            Name=mediatype.name
        )


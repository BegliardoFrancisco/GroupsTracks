from pydantic import BaseModel
from src.domain.models.media_type import MediaType


class MediaTypeResponses(BaseModel):
    id: int
    name: str


class ConverterMediaType:
    @staticmethod
    async def to_response(mediatype: MediaType) -> MediaTypeResponses:
        return MediaTypeResponses(
            id=mediatype.id,
            name=mediatype.name
        )

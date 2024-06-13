from pydantic import BaseModel
from src.domain.models.genre import Genre


class GenreResponses(BaseModel):
    id: int
    name: str


class ConverterGenre:
    @staticmethod
    async def to_response(genre: Genre) -> GenreResponses:
        return GenreResponses(
            id=genre.id,
            name=genre.name
        )
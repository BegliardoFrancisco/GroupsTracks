from src.infraestructure.entities.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from src.domain.models.genre import Genre


class GenresDAO(Base):
    __tablename__ = "genres"
    GenreId: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str]

    async def from_domain(self, ) -> Genre:
        return Genre(
            id=self.GenreId,
            name=self.Name
        )

    @staticmethod
    async def from_dto(genre: Genre) -> 'GenresDAO':
        return GenresDAO(
            GenreId=genre.id,
            Name=genre.name
        )

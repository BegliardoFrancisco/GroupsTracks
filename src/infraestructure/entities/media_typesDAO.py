from src.infraestructure.entities.base import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class MediaTypeDAO(Base):
    __tablename__ = "media_types"
    MediaTypeId: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str]

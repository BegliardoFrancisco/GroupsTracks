from pydantic import BaseModel
from typing import Optional


class ArtistRequest(BaseModel):
    id: Optional[int]
    name: str

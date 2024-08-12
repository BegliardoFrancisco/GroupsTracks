from pydantic import BaseModel
from typing import Optional


class NewArtistRequest(BaseModel):
    name: str


class ArtistRequestUpdate(BaseModel):
    id: int
    name: str

    def if_with_id(self):
        return self.id is None or self.id == 0


from src.domain.repositories.genres_repository import GenreRepositories
from src.domain.repositories.media_type_repository import MediaTypeRepositories
from src.domain.models.play_list import PlayList
from src.domain.repositories.playlist_repository import PlayListRepositories
from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from . import engine
from sqlalchemy import select, delete, update

class PlayListRepositoryImpl(PlayListRepositories):
    
    def __init__(self, genre_repository: GenreRepositories ,media_type_repository: MediaTypeRepositories):
        super().__init__(genre_repository, media_type_repository)
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_all_playlist(self) -> List[PlayList]:
       pass
    
    async def get_playlist_id(self, id: int) -> PlayList:
        pass

    async def add_playlist(self, playlist: PlayList) -> None:
       pass

    async def delete_playlist(self, playlist_id: int) -> None:
        pass

    async def update_playlist(self, playlist: PlayList) -> None:
        pass
